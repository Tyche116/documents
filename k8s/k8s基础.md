### 核心组件

- etcd：保存了整个集群的状态；
- apiserver：提供了资源操作的唯一入口，并提供认证、授权、访问控制、API 注册和发现等机制；
- controller manager：负责维护集群的状态，比如故障检测、自动扩展、滚动更新等；
- scheduler：负责资源的调度，按照预定的调度策略将 Pod 调度到相应的机器上；
- kubelet：负责维护容器的生命周期，同时也负责 Volume（CVI）和网络（CNI）的管理；
- Container runtime：负责镜像管理以及 Pod 和容器的真正运行（CRI）；
- kube-proxy：负责为 Service 提供 cluster 内部的服务发现和负载均衡



![v2-eb385bf27a1b35c20ef7cae6d056251f_r](C:\Users\dell\Desktop\v2-eb385bf27a1b35c20ef7cae6d056251f_r.jpg)

除了核心组件，还有一些推荐的 Add-ons：

- kube-dns：负责为整个集群提供 DNS 服务
- Ingress Controller：为服务提供外网入口
- Heapster：提供资源监控
- Dashboard：提供 GUI
- Federation：提供跨可用区的集群
- Fluentd-elasticsearch：提供集群日志采集、存储与查询

## 基础概念

```
Kubernetes直接管理Pod而不是容器：
一个pod可以是一个容器，也可以是多个容器，例如你运行一个服务项目，其中需要使用nginx、mysql、tomcat，可以将这三个应用在同一个pod中，对他们提供统一的调配能力。
一个pod只能运行在一个主机上，而一个主机上可以有多个pod。
```

##### 服务

```
一个Pod只是一个运行服务的实例，随时可能在一个节点上挂掉，在另一个节点以一个新的IP启动一个新的Pod，因此不能以固定的IP和端口号对外提供服务。
要稳定地提供服务需要服务发现和负载均衡能力。每个Service会对应一个集群内部有效的虚拟VIP，集群内部通过VIP访问一个服务。
在K8s集群中微服务的负载均衡是由Kube-proxy负载均衡器来实现的。它是一个分布式代理服务器，在K8s的每个节点上都有一个。
```

##### 存储卷

```
K8s集群中的存储卷跟Docker的存储卷有些类似，只不过Docker的存储卷作用范围为一个容器，而K8s的存储卷的生命周期和作用范围是一个Pod。
每个Pod中声明的存储卷由Pod中的所有容器共享。
```

##### 运行

```
集群中 master 节点上运行三个进程：
分别是：kube-apiserver，kube-controller-manager和kube-scheduler。

群集每个node节点都运行两个进程：
kubelet，与Kubernetes Master进行通信。
kube-proxy，一个网络代理，反映每个节点上的Kubernetes网络服务。
```



在使用Docker时，可以使用docker run命令创建并启动一个容器。而在Kubernetes系统中对长时间运行容器的要求是：其主程序需要一直在前台执行。如果我们创建的Docker镜像的启动命令是后台执行程序，例如Linux脚本：
     nohup ./start.sh &
则在kubelet创建包含这个容器的Pod之后运行完该命令，即认为Pod执行结束，将立刻销毁该Pod。如果为该Pod定义了ReplicationController，则系统将会监控到该Pod已经终止，之后根据RC定义中Pod的replicas副本数量生成一个新的Pod。而一旦创建出新的Pod，就将在执行完启动命令后，陷入无限循环的过程中。这就是Kubernetes需要我们自己创建的Docker镜像以一个前台命令作为启动命令的原因。





### k8s常用命令

### Create a Cluster

minikube version

minikube start

kubectl version

kubectl cluster-info

kubectl get nodes

### Deploy an App

kubectl version

kubectl get nodes

kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1

kubectl get deployments

echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n"; 

kubectl proxy

curl http://localhost:8001/version

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}') 

echo Name of the Pod: $POD_NAME

### Exploring Your App

kubectl get pods

kubectl describe pods

echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n"; 

kubectl proxy

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}') 

echo Name of the Pod: $POD_NAME

curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/

kubectl logs $POD_NAME

kubectl exec $POD_NAME env

kubectl exec -ti $POD_NAME bash



### Exposing Your App

kubectl get pods

查看集群下的服务  kubectl get services

发布服务 kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080

重新查看集群下的服务 kubectl get services

查看服务详情 kubectl describe services/kubernetes-bootcamp

export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}') 

echo NODE_PORT=$NODE_PORT

curl $(minikube ip):$NODE_PORT



使用label

查label

kubectl describe deployment

带label查询

kubectl get pods -l run=kubernetes-bootcamp

带label查询

kubectl get services -l run=kubernetes-bootcamp



取pod名字

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}') 

echo Name of the Pod: $POD_NAME

kubectl label pod $POD_NAME app=v1

kubectl describe pods $POD_NAME

kubectl get pods -l app=v1

kubectl delete service -l run=kubernetes-bootcamp

kubectl get services

curl $(minikube ip):$NODE_PORT

kubectl exec -ti $POD_NAME curl localhost:8080



### Scaling Your App

kubectl get deployments

kubectl get rs

kubectl scale deployments/kubernetes-bootcamp --replicas=4

kubectl get deployments

kubectl describe deployments/kubernetes-bootcamp

kubectl describe services/kubernetes-bootcamp

export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}') 

echo NODE_PORT=$NODE_PORT

curl $(minikube ip):$NODE_PORT

kubectl scale deployments/kubernetes-bootcamp --replicas=2

kubectl get deployments

kubectl get pods -o wide

### update app

kubectl get deployments

kubectl get pods

kubectl describe pods

kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2

kubectl get pods

kubectl describe services/kubernetes-bootcamp

export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}') 

echo NODE_PORT=$NODE_PORT

curl $(minikube ip):$NODE_PORT

kubectl rollout status deployments/kubernetes-bootcamp

kubectl describe pods

kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10

kubectl get deployments

kubectl get pods

kubectl describe pods

kubectl rollout undo deployments/kubernetes-bootcamp

kubectl get pods

kubectl describe pods



### k8s配置文件以及管理对象

```
对象管理：
# 创建deployment资源
kubectl create -f nginx-deployment.yaml
# 查看deployment
kubectl get deploy
# 查看ReplicaSet
kubectl get rs
# 查看pods所有标签
kubectl get pods --show-labels
# 根据标签查看pods
kubectl get pods -l app=nginx
# 滚动更新镜像
kubectl set image deployment/nginx-deployment nginx=nginx:1.11
或者
kubectl edit deployment/nginx-deployment
或者
kubectl apply -f nginx-deployment.yaml
# 实时观察发布状态：
kubectl rollout status deployment/nginx-deployment
# 查看deployment历史修订版本
kubectl rollout history deployment/nginx-deployment
kubectl rollout history deployment/nginx-deployment --revision=3
# 回滚到以前版本
kubectl rollout undo deployment/nginx-deployment
kubectl rollout undo deployment/nginx-deployment --to-revision=3
# 扩容deployment的Pod副本数量
kubectl scale deployment nginx-deployment --replicas=10
# 设置启动扩容/缩容
kubectl autoscale deployment nginx-deployment --min=10 --max=15 --cpu-percent=80
```

### k8s镜像策略

```
containers:    
- name: uses-private-image      
  image: $PRIVATE_IMAGE_NAME      
  imagePullPolicy: Always      
  command: [ "echo", "SUCCESS" ]
```

k8s的配置文件中经常看到有imagePullPolicy属性，这个属性是描述镜像的拉取策略

1. `Always` 总是拉取镜像
2. `IfNotPresent` 本地有则使用本地镜像,不拉取
3. `Never` 只使用本地镜像，从不拉取，即使本地没有
4. 如果省略imagePullPolicy 镜像tag为 :latest 策略为`always` ，否则 策略为 `IfNotPresent`

### 部署类型

pod  : 最小执行调度单元

Deployment :部署无状态应用

Daemonset : 部署守护应用

Cronjob :部署定时任务

job : 部署定时任务

statefulset  : 部署有状态应用

service ,endpoint, ingress 为服务类型

### K8s端口port配置

##### port
port是k8s集群内部访问service的端口，外部流量不可访问，即通过clusterIP: port可以访问到某个service

##### nodePort
nodePort是外部访问k8s集群中service的端口，通过nodeIP: nodePort可以从外部访问到某个service。

##### targetPort
targetPort是pod的端口，从port和nodePort来的流量经过kube-proxy流入到后端pod的targetPort上，最后进入容器。

##### containerPort
containerPort是pod内部容器的端口，targetPort映射到containerPort。

![20191229100240484](H:\file\20191229100240484.png)

### k8s挂载卷



### k8s常用命令

制作启动有前台运行的镜像

sudo docker build -t flaskapi .

Dockerfile文件内容如下：

```
FROM py_flask
ENV LANG C.UTF-8
CMD ["sh","-c","cd /root/ && ./start.sh"]
```



查看ip地址  

kubectl get ep

查看pod环境变量

kubectl exec podname env

本机可访问k8s内http服务，外部不可访问

sudo iptables -P FORWARD ACCEPT

查看pod详细信息

kubectl get pods --all-namespaces -o wide