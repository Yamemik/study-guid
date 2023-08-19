# study-guid

## About project
### description
    профориентация школьников

### technical development tools
    Python, Django, SQLite

## Command py

### create venv and activate
    python -m venv venv - создание виртуального пространства
    source ./venv/bin/activate (linux) - перейти в свое окружение
    deactivate - выйти

### install library into venv
    python -m ensurepip --upgrade 

    pip install django
    pip install djangorestframework
    pip install markdown
    pip install django-filter

### command django
    django-admin startproject config . - создание проекта

    python manage.py startapp main - создание приложения 

    python manage.py migrate
    python manage.py makemigrations main 
    python manage.py createsuperuser

    python manage.py runserver - запуск сервера

### command python
    print(dir(__builtins__)) -- список аттрибутов (встроенные функции)
    print(help(list.__eq__))

### command git
    git add .
    git commit -m 'message'
    git push
    git push origin <name_branch>
    git merge <name_branch>

## About us
### by Yamemik
    https://github.com/Yamemik