# API для проекта "Yatube"

API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, 
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

## Как запустить проект:
- _Клонировать репозиторий и перейти в него в командной строке:_

```sh
git clone https://github.com/WorkHotRoad/api_final_yatube.git
cd api_final_yatube
```

- _Cоздать и активировать виртуальное окружение:_
```sh
python3 -m venv venv
source venv/bin/activate
```
- _Обновить или установить пакет pip_
```sh
python3 -m pip install --upgrade pip
```
- _Установить зависимости из файла requirements.txt:_
```sh
pip install -r requirements.txt
```
- _Создать и выполнить миграции:_
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
- _Запустить проект:_
```sh
python3 manage.py runserver
```
- _Перейти по адресу:_
```sh
http://127.0.0.1:8000/api/v1/
```
