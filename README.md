# study_guid

## description
    профориентация школьников

## technical development tools
    Python, Django, SQLite

## command py

### create venv and activate
    python -m venv venv - создание виртуального пространства
    source ./venv/bin/activate (linux) - перейти в свое окружение
    deactivate - выйти

### install library into venv
    pip install django

### command django
    django-admin startproject config . - создание проекта

    python manage.py startapp main - создание приложения 

    python manage.py migrate
    python manage.py makemigrations tests   

    python manage.py runserver - запуск сервера

### command git
    git add .
    git commit -m 'message'
    git push
    git push origin <name_branch>
    git merge <name_branch>