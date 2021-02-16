# twitter-clone


## Установка Django (Да, я знаю, что надоел, используя новый фреймворк с новым проектом):

```sh 
pip install django
```
Все.


## Запуск сервера
Переходите в корневую папку проекта, где располагается `manage.py` и запускаете его:
```sh
manage.py runserver
```
Или
```sh
python manage.py runserver
```
Все.


## Static & Templates
Все в корне проекта для вашего удобства:

`templates` - .html

`static` - статические файлы

Все.


## Шаблонизатор
* Подключение static-файлов:

1. В начало HTML-документа добавляете `{% load static %}`
2. `href="{% static 'путь_к_файлу' %}` 

Путь пишется с учетом того, что мы уже находимся в папке static, т.е если хотим подключить index.css из static, то link выглядит так: 

`<link rel="stylesheet" type="text/css" href="{% static 'main/index.css' %}">`

Все.


# Нормальное ТЗ:
NULL
