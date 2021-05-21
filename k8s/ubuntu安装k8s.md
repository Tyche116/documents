### ubuntu18安装k8s

##### 更新系统源

```sh
sudo apt upgrade
```

##### 更新软件包

```shell
sudo apt update
```

##### 安装docker

```shell
sudo apt-get install docker.io
```

##### 安装http工具

```shell
sudo apt-get install -y apt-transport-https curl
```

##### 安装k8s

```shell
sudo apt-get install -y kubelet kubeadm kubectl --allow-unauthenticated
```

##### 若出现：

```shell
Reading package lists... Done
Building dependency tree       
Reading state information... Done

No apt package "kubeadm", but there is a snap with that name.
Try "snap install kubeadm"


No apt package "kubectl", but there is a snap with that name.
Try "snap install kubectl"


No apt package "kubelet", but there is a snap with that name.
Try "snap install kubelet"

E: Unable to locate package kubelet
E: Unable to locate package kubeadm
E: Unable to locate package kubectl
```

表明系统镜像源中找不到k8s软件包

打开 

```shell
sudo vim /etc/apt/sources.list 
```

文件，添加阿里镜像源地址

deb https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial main

然后更新软件包

```shell
sudo apt-get update
```

执行安装k8s

```shell
sudo apt-get install -y kubelet kubeadm kubectl --allow-unauthenticated
```

出现

The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 6A030B21BA07F4FB

需要添加key

```shell
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add 
```

##### 测试

```shell
kubelet --version
```

Kubernetes v1.19.1

##### 关闭swap

sudo swapoff -a

sudo vim /etc/fstab

必须关闭swap，否则kubelet服务启动失败

##### 环境初始化

执行初始化命令

```shell
sudo kubeadm init --ignore-preflight-errors=Swap
```

因为k8s初始化需要从google拉取镜像，无法下载内容，需要从其他镜像源下载。

查看需要下载的镜像列表

```shell
kubeadm config images list 
```

```shell
k8s.gcr.io/kube-apiserver:v1.19.1
k8s.gcr.io/kube-controller-manager:v1.19.1
k8s.gcr.io/kube-scheduler:v1.19.1
k8s.gcr.io/kube-proxy:v1.19.1
k8s.gcr.io/pause:3.2
k8s.gcr.io/etcd:3.4.13-0
k8s.gcr.io/coredns:1.7.0
```

从阿里镜像源拉取需要的镜像

```shell
sudo docker pull registry.aliyuncs.com/google_containers/kube-apiserver:v1.19.1

sudo docker pull registry.aliyuncs.com/google_containers/kube-controller-manager:v1.19.1

sudo docker pull registry.aliyuncs.com/google_containers/kube-scheduler:v1.19.1

sudo docker pull registry.aliyuncs.com/google_containers/kube-proxy:v1.19.1

sudo docker pull registry.aliyuncs.com/google_containers/pause:3.2

sudo docker pull registry.aliyuncs.com/google_containers/etcd:3.4.13-0

sudo docker pull registry.aliyuncs.com/google_containers/coredns:1.7.0
```

修改tag成k8s执行init检查的镜像：

```shell
sudo docker tag registry.aliyuncs.com/google_containers/kube-apiserver:v1.19.1 k8s.gcr.io/kube-apiserver:v1.19.1

sudo docker tag registry.aliyuncs.com/google_containers/kube-controller-manager:v1.19.1 k8s.gcr.io/kube-controller-manager:v1.19.1

sudo docker tag registry.aliyuncs.com/google_containers/kube-scheduler:v1.19.1 k8s.gcr.io/kube-scheduler:v1.19.1

sudo docker tag registry.aliyuncs.com/google_containers/kube-proxy:v1.19.1 k8s.gcr.io/kube-proxy:v1.19.1

sudo docker tag registry.aliyuncs.com/google_containers/pause:3.2 k8s.gcr.io/pause:3.2

sudo docker tag registry.aliyuncs.com/google_containers/etcd:3.4.13-0 k8s.gcr.io/etcd:3.4.13-0

sudo docker tag registry.aliyuncs.com/google_containers/coredns:1.7.0 k8s.gcr.io/coredns:1.7.0
```

删除docker重复的镜像tag：

```shell
 sudo docker rmi registry.aliyuncs.com/google_containers/kube-proxy:v1.19.1

 sudo docker rmi registry.aliyuncs.com/google_containers/kube-apiserver:v1.19.1

 sudo docker rmi registry.aliyuncs.com/google_containers/kube-controller-manager:v1.19.1

 sudo docker rmi registry.aliyuncs.com/google_containers/kube-scheduler:v1.19.1

 sudo docker rmi registry.aliyuncs.com/google_containers/etcd:3.4.13-0

 sudo docker rmi registry.aliyuncs.com/google_containers/coredns:1.7.0

 sudo docker rmi registry.aliyuncs.com/google_containers/pause:3.2
```

重新执行init

```shell
sudo kubeadm init --kubernetes-version=v1.19.1 --pod-network-cidr=192.168.1.90/16
```



sudo docker info

sudo vim /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

sudo vim /var/lib/kubelet/config.yaml



### 设置kubelet开机自启

```shell
systemctl enable kubelet.service
```

### 初始化后配置

在当前的用户的Home目录下创建.kube目录(这个目录中保存我们的连接配置，kubectl和kubeApi进行https通讯，所以有一些缓存需要保存以及一些认证文件)

```
mkdir -p $HOME/.kube
```

拷贝集群管理员的配置文件到这个目录下

```
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
```

授予权限(所有者 所有组授予当前的用户)

```
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```



### 网络配置

下载源码：

git clone https://github.com/coreos/flannel.git

在Documentation目录下找到 kube-flannel.yml

安装flannel  

sudo kubectl apply -f kube-flannel.yml



## K8s命令

重启 

sudo kubeadm reset

systemctl enable kubelet 

systemctl restart kubelet

sudo kubeadm init --kubernetes-version=v1.19.1 --pod-network-cidr=192.168.1.90/16



systemctl status kubelet 查看kubelet服务

journalctl -xefu kubelet 查看systemd日志

```
systemctl daemon-reload  
systemctl restart kubelet
```





sudo kubeadm init --kubernetes-version=v1.19.1 --pod-network-cidr=192.168.1.90/16



查看集群信息

kubectl cluster-info

查看pod信息

kubectl get pods --all-namespaces



## 设置 Master 为可调度节点

默认情况下，`Master` 不参与 `Pod` 调度，也就是说不会在 `Master` 节点上部署其他非系统 `Pod`。我们可以使用一下命令调整这个策略：

```
允许 Master 部署 Pod kubectl taint nodes localhost.master node-role.kubernetes.io/master- --overwrite

禁止 Master 部署 Pod kubectl taint nodes localhost.master node-role.kubernetes.io/master=:NoSchedule --overwrite 

其中 localhost.master 是操作的节点名称
```

### 安装node节点

##### 修改虚拟机node节点的hostname

永久修改

```
sudo vim /etc/hostname
sudo reboot
```

##### 关闭SWAP

```
swapoff   -a

vim /etc/fstab # 注释掉SWAP分区项，即可 # swap was on /dev/sda11 during installation # UUID=0a55fdb5-a9d8-4215-80f7-f42f75644f69 none  swap    sw      0       0
```

##### 执行安装k8s

```shell
sudo apt-get install -y kubelet kubeadm kubectl --allow-unauthenticated
```

##### 载入镜像

在部署每个节点的时候,都需要载入以下两个镜像

```
gcr.io/google_containers/pause:3.2
gcr.io/google_containers/kube-proxy:v1.19.1
```

##### 启动 kubectl

kubectl 是每台机器上的节点控制服务，所以 `join` 前要保证它在工作：

```bash
systemctl daemon-reload
systemctl enable kubelet
systemctl restart kubelet
```

##### 网络配置

下载源码：

git clone https://github.com/coreos/flannel.git

在Documentation目录下找到 kube-flannel.yml

安装flannel  

sudo kubectl apply -f kube-flannel.yml

##### 加入群集

在node节点执行

kubeadm join 192.168.6.223:6443 --token 697jw3.97qlcoanero8vo46 \
    --discovery-token-ca-cert-hash sha256:a8d7b7fbcc1eaa20191f44b2841a75bc46e92ffa3a53c7dd299357c82cf29b8e 

##### 查看pod

```
chain@master:~/k8s$ kubectl get nodes
NAME     STATUS   ROLES    AGE     VERSION
master   Ready    master   21m     v1.19.1
node1    Ready    <none>   7m50s   v1.19.1
node2    Ready    <none>   6m21s   v1.19.1
```

##### 验证网络

正常情况下，安装 `Pod` 网络成功之后，各个节点的 `Pod` 的网络是可以 `ping` 通的：

```bash
# 先找出两个在不同节点的 Pod 分配到的 IP（没有的话部署一个）
[root@localhost ~]# kubectl get pod -o wide --all-namespaces
NAMESPACE     NAME                             READY   STATUS    RESTARTS   AGE     IP              NODE     NOMINATED NODE   READINESS GATES
kube-system   coredns-f9fd979d6-q49z7          1/1     Running   0          23m     192.168.0.3     master   <none>           <none>
kube-system   coredns-f9fd979d6-xb5f7          1/1     Running   0          23m     192.168.0.2     master   <none>           <none>
kube-system   etcd-master                      1/1     Running   0          23m     192.168.6.223   master   <none>           <none>
kube-system   kube-apiserver-master            1/1     Running   0          23m     192.168.6.223   master   <none>           <none>
kube-system   kube-controller-manager-master   1/1     Running   0          23m     192.168.6.223   master   <none>           <none>
kube-system   kube-flannel-ds-c6dpg            1/1     Running   0          3m45s   192.168.6.223   master   <none>           <none>
kube-system   kube-flannel-ds-dkfnd            1/1     Running   0          3m45s   192.168.6.224   node1    <none>           <none>
kube-system   kube-flannel-ds-ljjms            1/1     Running   0          3m45s   192.168.6.225   node2    <none>           <none>
kube-system   kube-proxy-bvhbf                 1/1     Running   0          10m     192.168.6.224   node1    <none>           <none>
kube-system   kube-proxy-jkkm5                 1/1     Running   0          23m     192.168.6.223   master   <none>           <none>
kube-system   kube-proxy-ns226                 1/1     Running   0          9m1s    192.168.6.225   node2    <none>           <none>
kube-system   kube-scheduler-master            1/1     Running   0          23m     192.168.6.223   master   <none>           <none>

# 在 Master 尝试 Ping 另一个节点内 Pod 的 IP
chain@master:~/k8s$ ping 192.168.6.225
PING 192.168.6.225 (192.168.6.225) 56(84) bytes of data.
64 bytes from 192.168.6.225: icmp_seq=1 ttl=64 time=0.308 ms
64 bytes from 192.168.6.225: icmp_seq=2 ttl=64 time=0.388 ms
64 bytes from 192.168.6.225: icmp_seq=3 ttl=64 time=0.334 ms
64 bytes from 192.168.6.225: icmp_seq=4 ttl=64 time=0.317 ms
^C
--- 192.168.6.225 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3062ms
rtt min/avg/max/mdev = 0.308/0.336/0.388/0.038 ms

# 在 Master Pod 内尝试 Ping 另一个节点内 Pod 的 IP
[root@localhost ~]# kubectl exec -ti http-test-dm-bcd8d9b5b-7kmxq bash
[root@http-test-dm-bcd8d9b5b-7kmxq /]# ping 10.244.2.95
PING 10.244.2.95 (10.244.2.95) 56(84) bytes of data.
64 bytes from 10.244.2.95: icmp_seq=1 ttl=62 time=1.60 ms
64 bytes from 10.244.2.95: icmp_seq=2 ttl=62 time=1.69 ms
64 bytes from 10.244.2.95: icmp_seq=3 ttl=62 time=1.98 ms
64 bytes from 10.244.2.95: icmp_seq=4 ttl=62 time=2.08 ms
--- 10.244.2.95 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3001ms
rtt min/avg/max/mdev = 1.600/1.842/2.089/0.204 ms
```







清理运行在k8s群集中的pod

kubectl delete node --all



### 问题集

kubectl get nodes
Unable to connect to the server: dial tcp 192.168.6.137:6443: connect: no route to host

```
 mkdir -p $HOME/.kube
 sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
 sudo chown $(id -u):$(id -g) $HOME/.kube/config
```



sudo kubectl get nodes
The connection to the server localhost:8080 was refused - did you specify the right host or port?

原因是kubectl命令需要使用kubernetes-admin来运行，解决方法如下，将主节点中的【/etc/kubernetes/admin.conf】文件拷贝到从节点相同目录下

```
 mkdir -p $HOME/.kube
 sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
 sudo chown $(id -u):$(id -g) $HOME/.kube/config
```



## 指定Node

通过nodeSelector，一个Pod可以指定它所想要运行的Node节点。

首先给Node加上标签：

```
kubectl label nodes <your-node-name> disktype=ssd
```

接着，指定该Pod只想运行在带有`disktype=ssd`标签的Node上：

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    disktype: ssd
```

## k8s容器内无法ping同外网和其他pod

iptables -P FORWARD ACCEPT