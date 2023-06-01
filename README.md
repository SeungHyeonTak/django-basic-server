## Prerequisite
+ python >= 3.9
+ Django >= 4.2
+ mysql (latest)

### .env
```shell
DEBUG=
SECRET_KEY=

# 슬랙
SLACK_USER_OAUTH_TOKEN=
SLACK_BOT_USER_OAUTH_TOKEN=
SLACK_WEB_HOOK_URL=

# 데이터베이스
DB_HOST=
DB_NAME=
DB_PASSWORD=
DB_PORT=
DB_USER=
MYSQL_ROOT_PASSWORD=
```

## Usage

1. docker running with command
```shell
docker-compose up -d
```