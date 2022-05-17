# lab

## インストールについて
**Docker Desktop**には、**DockerとDocker-Compose**のどちらも入っているので、インストールすればどちらも使用可能。
## DockerとDocker-composeのインストール(Windows)
Windowsのエディションによってインストール方法が異なるので、それぞれ確認する。
### Windows10 Home Editionの場合
Windows 10 Home EditionでもWSL2をバックエンドにを使えばDockerをインストールすることが可能。
WSL2を有効化した状態で以下公式ドキュメントを参考にインストール→実行
[ダウンロードページ](https://docs.docker.com/desktop/windows/install/)
[Windows Home に Docker Desktop をインストール](https://docs.docker.jp/docker-for-windows/install-windows-home.html)
### Windows10 Professional等のHome Edition以外のバージョンの場合
Home Editionでは使用できないHyper-Vをバックエンドに動かすのでWSL2のセットアップはしなくても使用可能。
下記公式ドキュメントを参考にインストール→実行
[ダウンロードページ](https://docs.docker.com/desktop/windows/install/
[Windows に Docker Desktop をインストール](https://docs.docker.jp/docker-for-windows/install.html)

## DockerとDocker-composeのインストール(Mac)
Macの場合、特に必要なものがないのでそのまま下記公式ドキュメントに則ってインストール→実行
[ダウンロードページ](https://docs.docker.com/desktop/mac/install/)
[Mac に Docker Desktop をインストール](https://docs.docker.jp/docker-for-mac/install.html)


## DockerとDocker-composeのインストール(Linux)
Docker EngineとDocker-composeをそれぞれインストールする必要がある。
インストール方法については後に追記予定。
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
これでコンテナの中に入れるので、あとは通常のUbuntuと同じ。