# Project UH-Drill

### ローカル環境
- docker 20.10.20
- docker-compose 2.12.1
- git 2.34.1

### 作成する環境
- Python 3.11.0
- PostgreSQL 15
- nginx 1.23.2
- django 4.XX

### 環境の構築
```
$ git clone https://github.com/uhmfg-yuyasaito/uh-drill.git
```

### コンテナの構築
```
$ docker-compose build
```

### コンテナの作成と立ち上げ
```
$ docker-compose up -d
```

### コンテナ起動確認(windowsのDockerから確認してもOK)
```
$ docker ps -a
```

### アプリのコンテナに接続
```
$ docker-compose exec app bash
```

### Djangoインストールコマンド
```
$ docker-compose exec django /bin/bash
$ django-admin startproject uhdrill .
```

### 参考サイト
```
https://qiita.com/ftoshiki/items/1cb250a27bbbbaa5c719
https://zenn.dev/iroristudio/articles/0216072d2d1f24
```

### 参考サイト(エラー系)
```
https://www.askdjapy.com/vsc-error-message-import-django-db-could-not-be-resolved-from-source/
```
