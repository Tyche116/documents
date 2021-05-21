# 区块链网络的nginx转发部署

## 安装nginx

```
sudo apt-get install nginx
```

## 查看nginx安装是否带with-stream参数

```shell
nginx -V |grep with-stream
```

有with-stream参数，可以代理tcp协议



## 修改nginx主配置文件

```shell
vim /etc/nginx/nginx.conf
```

在文件后添加，示例为两个区块链节点之间转发的配置

```
stream{
    upstream node1{
        server  192.168.6.226:26656 max_fails=3 fail_timeout=10s;
    }
    upstream node2{
        server  192.168.6.227:26656 max_fails=3 fail_timeout=10s;
    }
    server{
        listen 10001;
        proxy_connect_timeout 20s;
        proxy_timeout 5m;
        proxy_pass node1;
    }
    server{
        listen 10002;
        proxy_connect_timeout 20s;
        proxy_timeout 5m;
        proxy_pass node2;
    }
}
```

其中10001，10002，加上nginx所在服务器的ip，配置给区块链节点的对外地址。种子节点的地址也要配置为nignx的地址加分配的端口。

例如：nginx主机ip为 192.168.6.228   开放10001，10002给节点node1，node2。

node1主机ip为 192.168.6.226 开放 26656， 其config.toml的 external_address = "192.168.6.228:10001"

node2主机ip为 192.168.6.227 开放 26656，其config.toml的 external_address = "192.168.6.228:10002"，

seeds = "541dba3eba349e73477d1e9b61186b75d524eebe@192.168.6.228:10001"

## 测试配置文件是否正确

```shell
nginx -t -c /etc/nginx/nginx.conf
```

## 启动nginx服务

```shell
systemctl start nginx.service
```

## 查看启动的nginx服务

```shell
systemctl status nginx.service
```



若出现 nginx Failed to read PID from file /run/nginx.pid: Invalid argument 的报错，

```
mkdir -p /etc/systemd/system/nginx.service.d
printf "[Service]\nExecStartPost=/bin/sleep 0.1\n" > /etc/systemd/system/nginx.service.d/override.conf
```

然后

```
systemctl daemon-reload
systemctl restart nginx.service
```



## 测试nginx的连通性

```
$ telnet 192.168.6.228 10001
Trying 192.168.6.228...
Connected to 192.168.6.228.
Escape character is '^]'.
```

出现"Connected to 192.168.6.228",说明连接成功





# 区块链接口服务flask的负载均衡部署

## 添加配置文件

先转到http转发配置目录

```
cd /etc/nginx/conf.d
```

新建配置文件

```
touch flask-8004.conf
```

编辑并添加配置 vim flask-8004.conf

```
upstream flask {
        server 192.168.6.226:8004;
        server 192.168.6.227:8004;
}
server {
        listen 8008;
        server_name chain_flask;
        location / {
        # 后端的Web服务器可以通过X-Forwarded-For获取用户真实IP
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X_Nginx_Proxy true;
        proxy_redirect off;
        proxy_pass http://flask;
        }
}
```

其中 

```
upstream flask {
        server 192.168.6.226:8004;
        server 192.168.6.227:8004;
}
```

为两个用来的区块链接口服务的地址，负载均衡的方式为轮询。

## 重启nginx服务

```
service nginx restart
```

## 测试

在其他机器访问nginx监听的ip和端口测试

```
 curl -H "Content-Type: application/json" -X POST -d '{"token":"3Q1EbvdpmTssybyNu3pfGke1SqG2NmtBHd5qwjXYeHvV","data":{"bankID":"NK0001","areaID":"320102","startTime":1599375600000,"endTime":1599446558000}}' "http://192.168.6.228:8008/blockchain/bank_supervision/queryStatistics
```