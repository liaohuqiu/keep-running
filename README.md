###pygments for PHP

In fact, it is a RPC server, based on [Cube RPC for python](https://github.com/liaohuqiu/cube-rpc-python). 

It providers code highlight service.

####installation

```bash
(sudo) python setup.py install  # intall dependencies
python pygments-server.py       # start server
```

####php call example

Using [Cube-php](https://github.com/liaohuqiu/cube-php), You can call the service in PHP like:

```php
<?php
$t1 = microtime(true);
$end_point = 'pygments@tcp:127.0.0.1:2016';
$proxy = MCore_Proxy_CubeProxy::getInstance($end_point);
$data = array();
$data['lang'] = 'php';
$data['code'] = '<?php phpinfo?>';
$ret = $proxy->request('highlight', $data);
$t2 = microtime(true);
echo $t2 - $t1, "\n";
var_export($ret);
```
