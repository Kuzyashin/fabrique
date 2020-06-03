## Тестовое задание для "Фабрика Решений" 


Расчётное время на выполнение тестового задания: 3-4 часа, время засекается нестрого. Приступить к выполнению тестового задания можно в любое удобное для вас время.

У текущего тестового задания есть только общее описание требований, конкретные детали реализации остаются на усмотрение разработчика.

Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: `Django 2.2.10`, `Django REST framework`.

Результат выполнения задачи:
- исходный код приложения в `github` (только на `github`, публичный репозиторий)
- инструкция по разворачиванию приложения (в `docker` или локально)
- документация по API




## Deploy on production

`create production.py from template.production.py`

`virtualenv --python=python3 --no-site-packages ./.env`

`.env/bin/pip install -r requirements.txt`

`.env/bin/pip install gunicorn`

`.env/bin/python manage.py migrate`

`.env/bin/python manage.py collectstatic`


### Add conf for nginx
```
server {
    listen 80;
    client_max_body_size 4G;
    server_name www.foo.bar;
    error_log  /foo/bar/backend/logs/nginx_error.log;
    access_log  /foo/bar/backend/logs/nginx_access.log;
    keepalive_timeout 5;
    charset utf-8;

    root /foo/bar/backend;

    location / {
        proxy_read_timeout 1200;
        proxy_connect_timeout 1200;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";


        proxy_pass http://127.0.0.1:8000;
    }

    location /static/ {
        alias /foo/bar/backend/public/static/;
    }
    location /media/ {
        alias /foo/bar/backend/public/media/;
    }
}
```
Enable config `ln -s /etc/nginx/sites-available/PROJECT_NAME.conf /etc/nginx/sites-enabled/`

Test configs `nginx -t`

`service nginx restart`


### Add conf for supervisor
```
[program:backend]
command=/foo/bar/backend/.env/bin/gunicorn project.wsgi:application -c /foo/bar/backend/configs/gunicorn.conf.py --pid=/foo/bar/backend/pids/gunicorn.pid --log-file /foo/bar/backend/logs/gunicorn.log
directory=/foo/bar/backend/
user=$USER
autorestart=true
startretries=3
stdout_logfile = /foo/bar/backend/logs/gunicorn_out.log
stderr_logfile = /foo/bar/backend/logs/gunicorn_err.log

```
`supervisorctl reread`

`supervisorctl update`

`supervisorctl reload`

`supervisorctl status`


## Deploy on local machine


`virtualenv --python=python3 --no-site-packages ./.env`

`.env/bin/pip install -r requirements.txt`

`.env/bin/python manage.py migrate`

`.env/bin/python manage.py runserver`


# Документация 

http://localhost:8000/api/redoc/