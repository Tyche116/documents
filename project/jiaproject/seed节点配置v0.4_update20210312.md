# 图灵链配置

人行节点配置为两台机器，两个开放的公用端口，配置四个节点。其中两个节点对商业银行开放p2p端口，两个节点运行在人行内部网络。

## 安装docker

1. 下载或准备docker离线安装包

   wget https://download.docker.com/linux/static/stable/x86_64/docker-17.03.2-ce.tgz

2. 解压安装包

   tar xzvf docker-17.03.2-ce.tgz

3. 移动docker目录

   cp docker/* /usr/bin/

4. docker root 路径修改
   mkdir /etc/docker /home/docker-data -p
   cat  /etc/docker/daemon.json 
   {
		"graph":"/home/docker-data"
   }

   
   
6. 启动docker daemon

   dockerd

7. 安装成功测试

   docker ps -a

   测试无问题将dockerd改成后台运行

   dockerd &

## 导入docker镜像

1. 准备图灵链的镜像tendermint_nk.tar，区块链服务接口镜像py_flask.tar

2. docker加载镜像

     docker load < py_flask.tar

     docker load < tendermint_nk_last.tar

## 初始化环境

1. 创建项目文件夹

   mkdir /home/chain/turingchain -p
   
   添加项目目录到系统

    vim /etc/profile

   在文件最后添加：PROJDIR=/home/chain/turingchain

   运行 source /etc/profile，让修改生效

2. 将依赖文件夹cryptoconditions，turingchaindb，scripts导入项目文件夹PROJDIR下
   cp -r cryptoconditions turingchaindb scripts /home/chain/turingchain



3. 修改区块链开机启动脚本，/home/chain/turingchain/scripts/下的startChainService.sh文件。
   vi /home/chain/turingchain/scripts/startChainService.sh

   示例文件启动了四个节点，人行配置为两台机器两个节点，修改为：

   ```
   echo "start ==> docker"
   dockerd &
   
   sleep 2s
   sh /home/chain/turingchain/scripts/start_tender1.sh &
   sleep 2s
   sh /home/chain/turingchain/scripts/start_tender2.sh &
   
   sleep 2s
   echo "start ==> flask"
   docker start flask
   ```
   
   其中/home/chain/turingchain/要修改为每台机器设定的路径
   
   start_tender1.sh示例如下：
   
   ```
   echo "start ==> tender1"
   docker start tender1
   
   sleep 2s
   docker exec tender1 bash -c 'sh /root/start.sh' &
   ```
   
   

## 配置区块链的节点(root)

1. 人行要配置的节点容器名为一台机器tender1

2. echo $PROJDIR  保证 PROJDIR=/home/chain/turingchain，防止路径出错

3. 一台机器生成两个节点的tendermint配置文件

   docker run -it --rm -v $PROJDIR/tender1:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender2:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender3:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender4:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender5:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender6:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender7:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender8:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender9:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender10:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender11:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender12:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender13:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender14:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender15:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender16:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender17:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender18:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender19:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender20:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender21:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender22:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender23:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender24:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender25:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender26:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender27:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender28:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender29:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender30:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender31:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender32:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender33:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender34:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender35:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender36:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender37:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender38:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender39:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender40:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender41:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender42:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender43:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender44:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender45:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender46:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender47:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender48:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender49:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init
   docker run -it --rm -v $PROJDIR/tender50:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint init






   在$PROJDIR/下会有tender1 这个文件夹，目录结构示例：

   ```
   tender1
          .tendermint
                      config
                              addrbook.json
                              config.toml
                              genesis.json
                              priv_validator.json
                              node_key.json
                      data
   ```

   

4. 一台机器生成两个节点的turingchaindb配置文件

   docker run -it --rm -v $PROJDIR/tender1:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender2:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender3:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender4:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender5:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender6:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender7:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender8:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender9:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender10:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender11:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender12:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender13:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender14:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender15:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender16:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender17:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender18:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender19:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender20:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender21:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender22:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender23:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender24:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender25:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender26:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender27:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender28:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender29:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender30:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender31:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender32:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender33:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender34:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender35:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender36:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender37:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender38:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender39:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender40:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender41:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender42:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender43:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender44:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender45:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender46:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender47:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender48:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender49:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure
   docker run -it --rm -v $PROJDIR/tender50:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk turingchaindb configure

  

  

   

   填写配置时，一直回车默认选项即可

   

5. 查看种子节点的nodeid，（例如将tender1节点设为种子节点）

   docker run -it --rm -v $PROJDIR/tender1:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender2:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender3:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender4:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender5:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender6:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender7:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender8:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender9:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk  tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender10:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender11:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender12:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender13:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender14:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender15:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender16:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender17:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender18:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender19:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender20:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender21:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender22:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender23:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender24:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender25:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender26:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender27:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender28:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender29:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender30:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender31:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender32:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender33:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender34:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender35:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender36:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender37:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender38:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender39:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender40:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender41:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender42:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender43:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender44:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender45:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender46:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender47:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender48:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender49:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   docker run -it --rm -v $PROJDIR/tender50:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions tendermint_nk tendermint show_node_id
   


   例如返回的nodeid : *12b1b55e022470803cd8920c79b80dd8e5636083*
 tender1:	12b1b55e022470803cd8920c79b80dd8e5636083    "local_node_id": "12b1b55e022470803cd8920c79b80dd8e5636083"
 tender2:	3183606b1ada12e3caadb9b57ed7d44d652ba6ce    "local_node_id": "3183606b1ada12e3caadb9b57ed7d44d652ba6ce"
 tender3:	78473573623fc8b684d0ea483c52471ebc4c945e    "local_node_id": "78473573623fc8b684d0ea483c52471ebc4c945e"
 tender4:	2701b928b21f7d7ba884ea557a3779c7252219ef    "local_node_id": "2701b928b21f7d7ba884ea557a3779c7252219ef"
 tender5:	135a4e624f53bf9c59e9bb8439c9e072f1589f22    "local_node_id": "135a4e624f53bf9c59e9bb8439c9e072f1589f22"
 tender6:	33cc7a728dd068201ebfaa42a21b08b52e419fb0    "local_node_id": "33cc7a728dd068201ebfaa42a21b08b52e419fb0"
 tender7:	98adb539ec70a0b61f7443fa6c7ec007a5f99b09    "local_node_id": "98adb539ec70a0b61f7443fa6c7ec007a5f99b09"
 tender8:	14b5c8a802f2a8346153a9bf36d2bdd952ee3e27    "local_node_id": "14b5c8a802f2a8346153a9bf36d2bdd952ee3e27"
 tender9:	54b4cefaf88e4de7f17f610723dac04d671fb9b7    "local_node_id": "54b4cefaf88e4de7f17f610723dac04d671fb9b7"
 tender10:	a4a4e08f7c5b8f4a38d9a8fc502132641159095f    "local_node_id": "a4a4e08f7c5b8f4a38d9a8fc502132641159095f"
 tender11:	640dd3f0adaa517f12d404b195589c51a6c3ce42    "local_node_id": "640dd3f0adaa517f12d404b195589c51a6c3ce42"
 tender12:	14e63f7cb6eb7e3f8a5e3c8be3853af9ef03f131    "local_node_id": "14e63f7cb6eb7e3f8a5e3c8be3853af9ef03f131"
 tender13:	53cfafd7ea56a68e76a56cefa081a55306498d9c    "local_node_id": "53cfafd7ea56a68e76a56cefa081a55306498d9c"
 tender14:	8c8639bca0aeb82c473fb6fb00cd55cb425f24e1    "local_node_id": "8c8639bca0aeb82c473fb6fb00cd55cb425f24e1"
 tender15:	1f78431b993e513ab0ad72932cbaec93551f2533    "local_node_id": "1f78431b993e513ab0ad72932cbaec93551f2533"
 tender16:	536553cba096154cc6de2c0c2241835c38789a79    "local_node_id": "536553cba096154cc6de2c0c2241835c38789a79"
 tender17:	39b52fe3ebeeb8add321eb26b9d80d56e09bb184    "local_node_id": "39b52fe3ebeeb8add321eb26b9d80d56e09bb184"
 tender18:	87156dce832754ec277ac97620e3c6e67ea0f70e    "local_node_id": "87156dce832754ec277ac97620e3c6e67ea0f70e"
 tender19:	5dc545a9035508deb7ce248ddafba9a686cc42a5    "local_node_id": "5dc545a9035508deb7ce248ddafba9a686cc42a5"
 tender20:	a89b2ba0ff531325d3bdb94f86164935fb6417d7    "local_node_id": "a89b2ba0ff531325d3bdb94f86164935fb6417d7"
 tender21:	860aec96bcc198ed67be6c602be28c5b2c72f1dc    "local_node_id": "860aec96bcc198ed67be6c602be28c5b2c72f1dc"
 tender22:	2f51a6af7ac35de96bf8f5ea2bb81fe90618be4a    "local_node_id": "2f51a6af7ac35de96bf8f5ea2bb81fe90618be4a"
 tender23:	ddb6b4184dd6c9d6e9fe56dbb35d6185fe0bcb48    "local_node_id": "ddb6b4184dd6c9d6e9fe56dbb35d6185fe0bcb48"
 tender24:	459c9ff0adc7420b447b054fa7e3c63e1cc84b72    "local_node_id": "459c9ff0adc7420b447b054fa7e3c63e1cc84b72"
 tender25:	a8f36bbf23cd86402d07be15c2824869a3a4864f    "local_node_id": "a8f36bbf23cd86402d07be15c2824869a3a4864f"
 tender26:	c88f6230cc7386ec900d18ab6d6f723ee739b3b1    "local_node_id": "c88f6230cc7386ec900d18ab6d6f723ee739b3b1"
 tender27:	79ed930caab18bd698ef37a9ae6346141e9e3a1a    "local_node_id": "79ed930caab18bd698ef37a9ae6346141e9e3a1a"
 tender28:	f5d245ba983ae1b8db5890c4482af811b1dbfe94    "local_node_id": "f5d245ba983ae1b8db5890c4482af811b1dbfe94"
 tender29:	b5a57fb5a338d55e3f1b964ac8af8ef6d0adde7a    "local_node_id": "b5a57fb5a338d55e3f1b964ac8af8ef6d0adde7a"
 tender30:	5c7306df14e4206649bc45b189678ede7606c501    "local_node_id": "5c7306df14e4206649bc45b189678ede7606c501"
 tender31:	764293b6380b17eea7142673fc9868c3043277e6    "local_node_id": "764293b6380b17eea7142673fc9868c3043277e6"
 tender32:	940200f016f491ee50b37ce71ccc0adb642b8cba    "local_node_id": "940200f016f491ee50b37ce71ccc0adb642b8cba"
 tender33:	921a56939359a2e4489751e7a7f14679ba92a966    "local_node_id": "921a56939359a2e4489751e7a7f14679ba92a966"
 tender34:	7327f17f3e73b60ad1c2cf0f894ce9af3df5e0e1    "local_node_id": "7327f17f3e73b60ad1c2cf0f894ce9af3df5e0e1"
 tender35:	743661b486991cf0172e4c268d96aec01f0d9ff0    "local_node_id": "743661b486991cf0172e4c268d96aec01f0d9ff0"
 tender36:	c702955b1af92c06c3562fe7d3c6586406589022    "local_node_id": "c702955b1af92c06c3562fe7d3c6586406589022"
 tender37:	2084574c0e6954a44cc4fe6e935c167b7fe50599    "local_node_id": "2084574c0e6954a44cc4fe6e935c167b7fe50599"
 tender38:	3164f428caf811577060b10389b8e3273b0ce48b    "local_node_id": "3164f428caf811577060b10389b8e3273b0ce48b"
 tender39:	9a833814ccf793e4ab7c2dfc2e26d1a404b60d40    "local_node_id": "9a833814ccf793e4ab7c2dfc2e26d1a404b60d40"
 tender40:	50c64d1652e0e507be0e1df055d2dc4d7cc5ac09    "local_node_id": "50c64d1652e0e507be0e1df055d2dc4d7cc5ac09"
 tender41:	5eab2bf35af3606f139072481d3db02812baf8b4    "local_node_id": "5eab2bf35af3606f139072481d3db02812baf8b4"
 tender42:	8f3baf0e04ba485aa34511d319ba57d887ea7da0    "local_node_id": "8f3baf0e04ba485aa34511d319ba57d887ea7da0"
 tender43:	fc5f567ce8b7422836d92f019449b074af63a257    "local_node_id": "fc5f567ce8b7422836d92f019449b074af63a257"
 tender44:	2fd65ea1b9bbdbdc09688416e02999ec1f269568    "local_node_id": "2fd65ea1b9bbdbdc09688416e02999ec1f269568"
 tender45:	abcfdc76ab57451411809ed7c4cf870c97e73e5b    "local_node_id": "abcfdc76ab57451411809ed7c4cf870c97e73e5b"
 tender46:	cdc47014cfee820ae24bae31e36e8a2a8aa41d37    "local_node_id": "cdc47014cfee820ae24bae31e36e8a2a8aa41d37"
 tender47:	64c7610256b5b134c5cfdd9226e587317250d9d4    "local_node_id": "64c7610256b5b134c5cfdd9226e587317250d9d4"
 tender48:	d69407881440abd7b74a1508b5bf5beca4516b9b    "local_node_id": "d69407881440abd7b74a1508b5bf5beca4516b9b"
 tender49:	190a92ebeaff0cf65cd7f5fd4ee8015ab19f629a    "local_node_id": "190a92ebeaff0cf65cd7f5fd4ee8015ab19f629a"
 tender50:	d1e64f3ddd7175a1cb922e65226e931feaf46504    "local_node_id": "d1e64f3ddd7175a1cb922e65226e931feaf46504"


   需要记下nodeid，方便之后配置p2p网络

   

6. 修改创始文件

   创世文件需要联盟的所有节点用同一个文件。

   vim $PROJDIR/tender1/.tendermint/config/genesis.json

   例如节点tender1初始化的创始文件 ：

   ```json
   {
     "genesis_time": "2020-09-10T03:56:32.508539997Z",
     "chain_id": "test-chain-YMOzgD",
     "consensus_params": {
       "block_size_params": {
         "max_bytes": "22020096",
         "max_txs": "10000",
         "max_gas": "-1"
       },
       "tx_size_params": {
         "max_bytes": "10240",
         "max_gas": "-1"
       },
       "block_gossip_params": {
         "block_part_size_bytes": "65536"
       },
       "evidence_params": {
         "max_age": "100000"
       }
     },
     "validators": [
       {
         "pub_key": {
           "type": "tendermint/PubKeyEd25519",
           "value": "9SjyV1HswCVvgqPYLahhFFUFthL/OKUotquKzHooexc="
         },
         "power": "10",
         "name": ""
       }
     ],
     "app_hash": ""
   }
   ```

   其中validators为联盟链初始节点列表，pub_key为节点tender1的公钥，power为权重。

   创世文件需要将所有的初始化的节点添加进来，例如将节点tender2添加：

   ```json
   {
     "genesis_time": "2020-09-10T03:56:32.508539997Z",
     "chain_id": "test-chain-YMOzgD",
     "consensus_params": {
       "block_size_params": {
         "max_bytes": "22020096",
         "max_txs": "10000",
         "max_gas": "-1"
       },
       "tx_size_params": {
         "max_bytes": "10240",
         "max_gas": "-1"
       },
       "block_gossip_params": {
         "block_part_size_bytes": "65536"
       },
       "evidence_params": {
         "max_age": "100000"
       }
     },
     "validators": [
       {
         "pub_key": {
           "type": "tendermint/PubKeyEd25519",
           "value": "9SjyV1HswCVvgqPYLahhFFUFthL/OKUotquKzHooexc="
         },
         "power": "10",
         "name": ""
       },{
         "pub_key": {
           "type": "tendermint/PubKeyEd25519",
           "value": "as321/8Mq2pE+rtQj5WkXIbFho0WtTLQfCx/wtW/EzU="
         },
         "power": "10",
         "name": ""
       }
     ],
     "app_hash": ""
   }
   ```

   将创建好的创始文件 genesis.json 拷贝到所有节点的配置目录  $PROJDIR/tender1/.tendermint/config/   $PROJDIR/tender2/.tendermint/config/ 覆盖原来的初始化的 genesis.json

cp genesis.json /home/chain/turingchain/tender2/.tendermint/config
cp genesis.json /home/chain/turingchain/tender3/.tendermint/config
cp genesis.json /home/chain/turingchain/tender4/.tendermint/config
cp genesis.json /home/chain/turingchain/tender5/.tendermint/config
cp genesis.json /home/chain/turingchain/tender6/.tendermint/config
cp genesis.json /home/chain/turingchain/tender7/.tendermint/config
cp genesis.json /home/chain/turingchain/tender8/.tendermint/config
cp genesis.json /home/chain/turingchain/tender9/.tendermint/config
cp genesis.json /home/chain/turingchain/tender10/.tendermint/config
cp genesis.json /home/chain/turingchain/tender11/.tendermint/config
cp genesis.json /home/chain/turingchain/tender12/.tendermint/config
cp genesis.json /home/chain/turingchain/tender13/.tendermint/config
cp genesis.json /home/chain/turingchain/tender14/.tendermint/config
cp genesis.json /home/chain/turingchain/tender15/.tendermint/config
cp genesis.json /home/chain/turingchain/tender16/.tendermint/config
cp genesis.json /home/chain/turingchain/tender17/.tendermint/config
cp genesis.json /home/chain/turingchain/tender18/.tendermint/config
cp genesis.json /home/chain/turingchain/tender19/.tendermint/config
cp genesis.json /home/chain/turingchain/tender20/.tendermint/config
cp genesis.json /home/chain/turingchain/tender21/.tendermint/config
cp genesis.json /home/chain/turingchain/tender22/.tendermint/config
cp genesis.json /home/chain/turingchain/tender23/.tendermint/config
cp genesis.json /home/chain/turingchain/tender24/.tendermint/config
cp genesis.json /home/chain/turingchain/tender25/.tendermint/config
cp genesis.json /home/chain/turingchain/tender26/.tendermint/config
cp genesis.json /home/chain/turingchain/tender27/.tendermint/config
cp genesis.json /home/chain/turingchain/tender28/.tendermint/config
cp genesis.json /home/chain/turingchain/tender29/.tendermint/config
cp genesis.json /home/chain/turingchain/tender30/.tendermint/config
cp genesis.json /home/chain/turingchain/tender31/.tendermint/config
cp genesis.json /home/chain/turingchain/tender32/.tendermint/config
cp genesis.json /home/chain/turingchain/tender33/.tendermint/config
cp genesis.json /home/chain/turingchain/tender34/.tendermint/config
cp genesis.json /home/chain/turingchain/tender35/.tendermint/config
cp genesis.json /home/chain/turingchain/tender36/.tendermint/config
cp genesis.json /home/chain/turingchain/tender37/.tendermint/config
cp genesis.json /home/chain/turingchain/tender38/.tendermint/config
cp genesis.json /home/chain/turingchain/tender39/.tendermint/config
cp genesis.json /home/chain/turingchain/tender40/.tendermint/config
cp genesis.json /home/chain/turingchain/tender41/.tendermint/config
cp genesis.json /home/chain/turingchain/tender42/.tendermint/config
cp genesis.json /home/chain/turingchain/tender43/.tendermint/config
cp genesis.json /home/chain/turingchain/tender44/.tendermint/config
cp genesis.json /home/chain/turingchain/tender45/.tendermint/config
cp genesis.json /home/chain/turingchain/tender46/.tendermint/config
cp genesis.json /home/chain/turingchain/tender47/.tendermint/config
cp genesis.json /home/chain/turingchain/tender48/.tendermint/config
cp genesis.json /home/chain/turingchain/tender49/.tendermint/config
cp genesis.json /home/chain/turingchain/tender50/.tendermint/config

   


7. 修改turingchaindb配置文件

   （注意 PROJDIR=/home/chain/turingchain）

   每台机器 vim $PROJDIR/tender1/.turingchaindb        vim $PROJDIR/tender2/.turingchaindb

   修改server : bind 为 0.0.0.0:9984

   修改tendermint:local_node_id为2c3fc1cefc71e3dbe3170f874e93fc7d01d58403

8. 添加白名单文件

   （注意 PROJDIR=/home/chain/turingchain）

   添加白名单文件到节点目录下 

   cp .turingchainwhitelist $PROJDIR/tender1

cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender1/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender2/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender3/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender4/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender5/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender6/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender7/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender8/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender9/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender10/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender11/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender12/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender13/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender14/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender15/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender16/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender17/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender18/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender19/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender20/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender21/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender22/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender23/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender24/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender25/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender26/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender27/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender28/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender29/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender30/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender31/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender32/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender33/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender34/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender35/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender36/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender37/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender38/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender39/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender40/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender41/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender42/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender43/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender44/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender45/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender46/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender47/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender48/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender49/
cp .turingchainwhitelist start.sh  /home/chain/turingchain/tender50/


9. 添加启动脚本

   （注意 PROJDIR=/home/chain/turingchain）

   添加启动脚本到节点目录下

   cp start.sh $PROJDIR/tender1



10. 修改节点配置文件

    vim $PROJDIR/tender1/.tendermint/config/config.toml

    在config.toml文件的**[p2p]**标签下，
    
    人行种子节点：
    
    a. 配置种子节点自己对外的地址：**external_address** = “9.48.47.109:4096”，其中9.48.47.109为对外IP地址，4096为对外的p2p端口。
    

   人行非种子节点：tender2
    vim $PROJDIR/tender2/.tendermint/config/config.toml
    a. 配置种子节点自己对外的地址：**external_address = "9.48.63.109:26658"，其中 9.48.63.109 为本机物理IP地址，26658为docker容器映射的本机物理p2p端口。
​    b. 配置种子节点地址：**seeds** = "12b1b55e022470803cd8920c79b80dd8e5636083@9.48.63.109:4096"，
       其中 12b1b55e022470803cd8920c79b80dd8e5636083 为种子节点node1的node_id，9.48.63.109:4096 为种子node1节点的本机物理IP地址和p2p端口号。    
​      


11. 创建docker容器并启动区块链

    （注意 PROJDIR=/home/chain/turingchain）

    每台机器创建tender1容器，其中-p 4096:26656 左边的26656端口为机器开放的端口，即种子节点tender1对外开放的端口

       docker run -it -p 9984:9984 -p 27027:27017 -p 4096:26656 -p 26667:26657 --name tender1 -v $PROJDIR/tender1:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions --log-opt max-size=50m --log-opt max-file=100 tendermint_nk  /bin/bash

    

    启动区块链程序：

    cd /root 

    ./start.sh

     

    每台机器创建tender2容器

      docker run -it -p 9985:9984 -p 27028:27017 -p 26666:26656 -p 26668:26657 --name tender2 -v $PROJDIR/tender2:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions --log-opt max-size=50m --log-opt max-file=100 tendermint_nk /bin/bash

    

    启动区块链程序：

    cd /root 

    ./start.sh

    

    p2p网络接通验证：

    看到有打印  
    ```
    v_num                                        module=consensus 1=(MISSING)\r\n","stream":"stdout","time":"2021-03-11T10:18:02.115413479Z"}
    NumPeers :                                   module=p2p 1=(MISSING)\r\n","stream":"stdout","time":"2021-03-11T10:18:03.156812828Z"}
    current peers :                              module=p2p Peer{MConn{172.17.0.1:4096}12b1b55e022470803cd8920c79b80dd8e5636083out}=(MISSING)\r\n","stream":"stdout","time":"2021-03-11T10:18:03.156869168Z"}
    Ensure peers                                 module=p2p numOutPeers=1 numInPeers=0 numDialing=0 numToDial=9\r\n","stream":"stdout","time":"2021-03-11T10:18:03.156883185Z"}
    We need more addresses. Sending pexRequest to random peer module=p2p peer=\"Peer{MConn{172.17.0.1:4096} 12b1b55e022470803cd8920c79b80dd8e5636083 out}\"\r\n","stream":"stdout","time":"2021-03-11T10:18:03.156893125Z"}
	
    ```
    内的 current peers表示节点在p2p网络上当前和本节点链接的节点。



12. 暂停或重启

    暂停 docker stop tender1

    重启 docker restart tender1

    docker exec tender1 bash -c 'sh /root/start.sh' &
	

## 配置区块链接口服务

tender1~tender20节点  bank_supervision非现场监管业务已用
进入flask容器
cd /root/bank_supervision/
python3 deploy_contract.py 
["12b1b55e022470803cd8920c79b80dd8e5636083","3183606b1ada12e3caadb9b57ed7d44d652ba6ce","78473573623fc8b684d0ea483c52471ebc4c945e",
"2701b928b21f7d7ba884ea557a3779c7252219ef","135a4e624f53bf9c59e9bb8439c9e072f1589f22","33cc7a728dd068201ebfaa42a21b08b52e419fb0",
"98adb539ec70a0b61f7443fa6c7ec007a5f99b09","14b5c8a802f2a8346153a9bf36d2bdd952ee3e27","54b4cefaf88e4de7f17f610723dac04d671fb9b7",
"a4a4e08f7c5b8f4a38d9a8fc502132641159095f","640dd3f0adaa517f12d404b195589c51a6c3ce42","14e63f7cb6eb7e3f8a5e3c8be3853af9ef03f131",
"53cfafd7ea56a68e76a56cefa081a55306498d9c","8c8639bca0aeb82c473fb6fb00cd55cb425f24e1","1f78431b993e513ab0ad72932cbaec93551f2533",
"536553cba096154cc6de2c0c2241835c38789a79","39b52fe3ebeeb8add321eb26b9d80d56e09bb184","87156dce832754ec277ac97620e3c6e67ea0f70e",
"5dc545a9035508deb7ce248ddafba9a686cc42a5","a89b2ba0ff531325d3bdb94f86164935fb6417d7"]


人行两台机器，可每台机器配一个或仅在一台机器部署一个接口服务

1. 拷贝http接口项目文件到容器目录下

   （注意 PROJDIR=/home/chain/turingchain）

   cp -r bank_supervision $PROJDIR/flask

2. 配置文件

   vim $PROJDIR/flask/bank_supervision/config.json 

   "bdb_root_url": "http://172.17.0.1:9984"  其中172.17.0.1设置为本机（物理地址ip，或者节点容器的ip，9984默认不变)

3. 配置公私钥（需自己重新生成才做如下操作）

   将需要的公钥文件public.pem或私钥文件private.pem放在 $PROJDIR/flask/bank_supervision下

   cp public.pem $PROJDIR/flask/bank_supervision
   
   cp private.pem $PROJDIR/flask/bank_supervision

   人行需要配置公钥，私钥文件。商业银行配置公钥文件。采用sha-512加解密。



4. 群组合约部署（仅在第一个种子节点部署合约即可，其他节点跳过）
   docker run -it -p 8004:8004 --name flask -v $PROJDIR/flask:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions --log-opt max-size=50m --log-opt max-file=100 py_flask /bin/bash

   或 docker exec -it flask bash

   部署合约 sh /root/bank_supervision/deploy.sh

   退出 容器 ctrl+P+Q

   重启flask容器 docker restart flask

   记下部署合约的地址，即$PROJDIR/flask/bank_supervision/config.json 文件中的bank_supervision_seivice

   测试：'a8fd8d61820b4d511adabccbb21dc95aa5bbb0d3a75957f62809cc446d10819b'
   生产：'11fd9c0a123d436f9f49cbc56cbc2bf1345d8cafb5c2b17ee857186f7695476d'
   
    
	
5. 启动docker容器，容器名为flask

   docker run -it -p 8004:8004 --name flask -v $PROJDIR/flask:/root -v $PROJDIR/turingchaindb:/usr/local/lib/python3.6/dist-packages/turingchaindb -v $PROJDIR/cryptoconditions:/usr/local/lib/python3.6/dist-packages/cryptoconditions --log-opt max-size=50m --log-opt max-file=100 py_flask sh /root/bank_supervision/start.sh

6. 群组合约地址配置（其他节点【商业银行端】配置合约地址）

   修改 $PROJDIR/flask/bank_supervision/config.json 文件中的bank_supervision_seivice为：

   测试：'a8fd8d61820b4d511adabccbb21dc95aa5bbb0d3a75957f62809cc446d10819b'
   生产：'11fd9c0a123d436f9f49cbc56cbc2bf1345d8cafb5c2b17ee857186f7695476d'

## 接口本地测试

区块链网络部署完成后，可用以下测试连通性

交易上链测试：

```
curl -H "Content-Type: application/json" -X POST -d '{"token": "3Q1EbvdpmTssybyNu3pfGke1SqG2NmtBHd5qwjXYeHvV","data": {"transactions": [{"transactionID": "20200903_NK0001_320102_ab566678_00012","bankID": "NK0001","areaID": "320102","acctEntity": "123test","txNums": 99,"merkleHash": "6d719c54bb6f1e806f60527ce5805562e2134164cdcdf2c90fa02860fb6bb5c3","fileHash":"c7e616822f366fb1b5e0756af498cc11d2c0862edcb32ca65882f622ff39de1b"}]}}' "http://172.17.0.1:8004/blockchain/bank_supervision/createTransaction"
```

其中172.17.0.1位本机ip地址，8004位http接口服务的端口

返回结果示例：

```
{
    "data": {
        "result": true,
        "status": "200",
        "tx_id": "04b3bd3d34d97b390179f6cded2bc322ac8cfe3e07c1facd70cc70632ac7d780"
    }
}
```

查询刚才上链的交易：

```
curl -H "Content-Type: application/json" -X POST -d '{"token":"3Q1EbvdpmTssybyNu3pfGke1SqG2NmtBHd5qwjXYeHvV","data":{"transactionID":"20200903_NK0001_320102_ab566678_00012","bankID":"NK0001","areaID":"320102","acctEntity": "123test"}}' "http://172.17.0.1:8004/blockchain/bank_supervision/queryTransaction"
```

其中172.17.0.1位本机ip地址，8004位http接口服务的端口

返回结果示例：

```
{
    "data": {
        "content": {
            "transaction": [
                {
                    "acctEntity": "123test",
                    "areaID": "320102",
                    "bankID": "NK0001",
                    "createTime": 1605508314899,
                    "fileHash": "c7e616822f366fb1b5e0756af498cc11d2c0862edcb32ca65882f622ff39de1b",
                    "merkleHash": "6d719c54bb6f1e806f60527ce5805562e2134164cdcdf2c90fa02860fb6bb5c3",
                    "transactionID": "20200903_NK0001_320102_ab566678_00012",
                    "txNums": 99
                }
            ]
        },
        "result": true,
        "status": "200"
    }
}
```



## 添加系统自动重启

1. 打开 vim  /etc/init.d/after.local  

2. 添加自启脚本 sh /home/chain/turingchain/scripts/startChainService.sh

3. 重启机器测试

   

## 添加新节点到区块链网络(忽略备用，暂不做操作)

1. 先将新节点配置完成

   先在新节点处初始环境，再完成新节点的配置工作。记录下新节点的node_id以及节点公钥public_key

   

2. 由已运行的区块链节点发起提案

   进入容器 docker exec -it tender1 bash

   发起提案：turingchaindb election new upsert-validator --private-key ~/.tendermint/config/priv_validator.json TR+xpREy9VR1HNBQwiw2SKYce5OwrGJJu9jmdsj04vo= 3 e8f463312b86abaabc71e609f93eca2902bcbc61

   其中TR+xpREy9VR1HNBQwiw2SKYce5OwrGJJu9jmdsj04vo=为新节点的公钥public_key，3为新节点的投票权重，e8f463312b86abaabc71e609f93eca2902bcbc61为新节点的node_id。

   执行完成后本次提案proposal会有交易tx_id : 3f82141d5bc3703b06816c76fe06be917cffc54f1f74e389aec1da25e64a2f8f

   

3. 由已运行的区块链网络节点的成员发起对提案的投票

   进入容器：docker exec -it tender2 bash

   投票：turingchaindb election approve --private-key ~/.tendermint/config/priv_validator.json 3f82141d5bc3703b06816c76fe06be917cffc54f1f74e389aec1da25e64a2f8f

   其中3f82141d5bc3703b06816c76fe06be917cffc54f1f74e389aec1da25e64a2f8f为提案执行后的tx_id

   所有已运行节点对提案的投票必须达到2/3权重，新节点才会成为validator，加入区块链网络

## 区块链接口服务更新

1. 暂停接口服务容器flask

   docker stop flask

2. 更新接口服务文件

   更新 $PROJDIR/flask/bank_supervision目录下的文件

3. 重启接口服务容器 flask

   docker restart flask

## 区块链清除数据
docker exec -it tender1 bash
ps -ef
docker exec -it tender2 bash
ps -ef


只保留MongoDB进程，清除数据
service mongodb start
turingchaindb drop
tendermint unsafe_reset_all

重启服务
sh /root/start.sh
