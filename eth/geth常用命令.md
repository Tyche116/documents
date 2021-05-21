ubuntu安装geth

```
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

windows安装geth

下载安装程序 https://geth.ethereum.org/downloads/ ，将geth等加入PATH环境变量







geth常用命令

初始化写入创始块

```
geth --datadir data0 init genesis.json
```

启动私有链节点

```
geth --datadir data --networkid 15 --syncmode 'full' --port 30312 --http --http.addr '0.0.0.0' --http.port 8545 --http.api 'personal,eth,net,web3,txpool,miner' --miner.gasprice '0' 
```



启一个geth通过rpc连接到一个节点

geth attach http://127.0.0.1:8545









remix共享本地文件夹

remixd -s E:/ethTest/remix --remix-ide http://remix.ethereum.org







geth --datadir data2 init 123.json

geth --datadir data init genesis.json

geth --datadir data --networkid 15 --syncmode 'full' --port 30312 --http --http.addr '0.0.0.0' --http.port 8545 --http.api 'personal,eth,net,web3,txpool,miner' --miner.gasprice 0 --unlock '0x1ff68648f2f78cb1531b0bd107afc008df779ab0' --password E:/ethTest/password.txt --mine --allow-insecure-unlock

geth --datadir data2 --networkid 15 --syncmode 'full' --port 30313 --http --http.addr '0.0.0.0' --http.port 8546 --http.api 'personal,eth,net,web3,txpool,miner' --miner.gasprice '0' --allow-insecure-unlock --unlock '0x1ff68648f2f78cb1531b0bd107afc008df779ab0' --password E:/ethTest/password.txt --mine console

geth --datadir data2 --networkid 15 --syncmode 'full' --port 30312 --http --http.addr '0.0.0.0' --http.port 8555 --http.api 'personal,eth,net,web3,txpool,miner' --miner.gasprice 0 --unlock '0x1ff68648f2f78cb1531b0bd107afc008df779ab0' --password E:/ethTest/password.txt --mine --allow-insecure-unlock

geth --bootnodes enode://99910207f0f14a0b87c6a2c5d03a04cffb42429c136d1e59f6a0add7d6337e32c9c0bb55fcca3e3c9a664e1a62c72eabdfb4d36d47b0f27fabf5c31053d8eab3@127.0.0.1:30312



web3.fromWei(eth.getBalance(eth.accounts[0]),'ether')

amount = web3.toWei(10,'ether')

10000000000000000000



personal.newAccount()

personal.listAccounts
eth.coinbase
miner.setEtherbase(eth.accounts[2])

miner.setEtherbase(personal.listAccounts[2])

eth.blockNumber

eth.getBlock(66)

eth.getTransaction("0x56555aba7f8a1b97f6630991f07327447fae5ec468c6160039e1d79185993cca")

eth.getBalance(eth.accounts[0])
eth.getBalance(eth.accounts[1])
eth.getBalance(eth.accounts[2])

personal.unlockAccount(eth.accounts[0])
personal.unlockAccount(eth.accounts[0], "123456")
personal.unlockAccount(eth.accounts[1], "123456")
personal.unlockAccount(eth.accounts[2], "123456")

eth.sendTransaction({from:eth.accounts[2],to:eth.accounts[0],value:10000000000000000000})

eth.sendTransaction({from:eth.accounts[0],to:eth.accounts[1],value:20000000000000000000})

eth.sendTransaction({from:eth.accounts[0],to:eth.accounts[2],value:30000000000000000000})



