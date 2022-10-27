# Tutoria 04 - Grupo 02

# 1 PASO CREAR UN ENTORNO VIRTUAL

virtualenv tutoria4Dswdm

cd Scripts

activate

cd..

# 2 PASO - instalación Django en ENV

pip install django==4.1.2

# 3 PASO - creación de un proyecto o CLONAR PROYECTO GIT

django-admin startproject T4Grupo02

cd T4Grupo02

# 4 PASO - migrate

python manage.py migrate

# 5 PASO - levantar el proyecto

python manage.py runserver

http://127.0.0.1:8000/

# 6 PASO - crear un superusuario

python manage.py createsuperuser

http://127.0.0.1:8000/admin

user: admin

pass: admin

# SEGMENTO DE AGREGACION / MODIFICACIONES MODULOS / CODIFICACION

# 7 PASO - creación de una aplicación

python manage.py startapp gt04pares


# 8 PASO - makemigrations

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/
