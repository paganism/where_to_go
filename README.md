# Куда пойти — Москва

Бэкэнд для сайта о самых интересных местах в Москве.

[Демка сайта](http://yurybelov.pythonanywhere.com/).

## Как запустить

* Скачайте код
* Перейдите в каталог проекта с файлом `manage.py`
* Экспортируйте переменные окружения
* Запустите веб-сервер `python3 manage.py runserver`
* Откройте в браузере
* Для загрузки интересных мест из json-файла используйте команду `python manage.py load_place файл.json`

## Настройки окружения. Пример:

```
export SECRET_KEY='my_secret_key'
export DEBUG=True
export SERVERNAMES='localhost 127.0.0.1'
export MEDIA_ROOT='media/'
export MEDIA_URL='/media/'
export STATIC_URL='/static/'
```

## Цели проекта

Код написан в учебных целях.