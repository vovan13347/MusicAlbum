# MusicAlbum
____
Получение и изменение данных о музыкальных исполнителях с помощью JSON и curl запросов

# Requirements
```
blinker==1.9.0
click==8.1.7
Flask==3.1.0
flask_sqlalchemy==3.0.3
greenlet==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3
```
# Примеры CURL запросов:
____

1. получение данных: `curl -X GET http://193.176.153.205:5000/albums`

2. получение данных: `curl -X POST http://193.176.153.205:5000/albums -H "Content-Type: application/json" -d "{\"title\": \"Back in Black\", \"band\": \"AC/DC\"}"`

3. обновление данных: `curl -X PUT http://193.176.153.205:5000/albums/8 -H "Content-Type: application/json" -d "{\"title\": \"Highway to Hell\", \"band\": \"AC/DC\"}"`

4. удаление данных: `curl -X DELETE http://193.176.153.205:5000/albums/8`

# name_service.service config
____
```
[Unit]
Description = text
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/projects/musicalbum
ExecStart=/projects/musicalbum/musicenv/bin/python3 name.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

```

3. перезапустить daemon командой:
`sudo systemctl daemon-reload`

4. активировать сервис, позволить ему стартовать во время запуска системы:
`sudo systemctl enable name_service.service`

5. запустить службу командой:
`sudo systemctl start name_service.service`

6. остановить активную службу:
`sudo systemctl stop name_service.service`

7. отключить автозапуск службы:
`sudo systemctl disable name_service.service`