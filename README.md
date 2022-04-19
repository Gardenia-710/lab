# lab
## DockerとDocker-composeのインストール(Windows)
詳しい手順は後で追記

## DockerとDocker-composeのインストール(Mac)
詳しい手順は後で追記

## Docker-compose upしてhostとrouterのコンテナを起動する
network-compose内部(docker-compose.ymlのあるディレクトリ)で
```
docker-compose up --build -d
```
を実行する。
dockerfileのbuildが行われて、ネットワークの設定が済んだコンテナが立ち上がる。

## 立ち上げたコンテナに入る
host4に入る場合
```
docker-compose exec host4 bash
```
これで