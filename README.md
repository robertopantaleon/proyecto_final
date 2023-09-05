# proyecto_final
Paso 1: Creamos la carpeta donde crearemos nuestro proyecto y la llamamos 
feedback_app

Paso 2: Accedemos a la carpeta  feedback_app a traves del cmd:
C:\Users\HONOR\desarrollo\programacion_upemor\feedback_app>

Paso 3: Verificamos las versiones de python instaladas
py --list

Paso 4: Creamos el entorno virtual:
py -3.10 -m venv venv

Paso 5: Activamos el entorno virtual:
venv\Scripts\activate.bat

Paso 6: Verificamos la lista de paquetes instalados y verificamos que no haya ninguno.
pip freeze

Paso 7: Instalamos django:
pip install django

Paso 8: Verificamos la lista de paquetes instalados, ya debe haber:
pip freeze

Paso 9: Creamos la carpeta feedback_site ejecutando el siguiente
comando dentro de la carpeta feedback_app:
django-admin startproject feedback_site

Paso 10: Abrimos la carpeta feedback_app desde Visual Studio Code 

Paso 11: Abrimos una nueva terminal en Visual Studio Code o en el cmd y nos pasamos a la 
carperta feedback_site y corremos el servidor.
python manage.py runserver

Paso 12: Abrimos el siguiente enlace en un navegador para acceder Django Administration
http://127.0.0.1:8000/admin 

Paso 13: Migramos los usuarios
python manage.py migrate 

Paso 14: Creamos el usuario root:
python manage.py createsuperuser

Paso 15: Escribimos los siguientes parametros para el usuario root:
Username (leave blank to use 'honor'): admin
Email address: admin@localhost.com
Password: admin
Password (again): admin
Bypass password validation and create user anyway? [y/N]: y

Paso 16: Volvemos a correr el servidor
python manage.py runserver 

Paso 17: Abrimos el siguiente enlace en un navegador para acceder Django Administration
http://127.0.0.1:8000/admin 
Escribimos los siguientes datos:
Username: admin
Password: admin

Paso 18: Detenemos el servidor
Presionamos ctrl + c dos veces

Paso 19: Hacemos los modelos creando la aplicacion dentro del proyecto django
python manage.py startapp feedback


archivo: models.py
from django.db import models

#Nota: no definimos llaves primarias por que en el archivo app.py de tu app,
se indica que se crean automáticamente.

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    surnames = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    carer = models.CharField(max_length=200)
    semester = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):  
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    datetimelimit = models.DateTimeField('date published')
    points = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
class Student_Task(models.Model):
    comments_teacher = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    qualification = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.comments_teacher

    
class Comments(models.Model):
    comments_student = models.CharField(max_length=1000)
    student_task = models.ForeignKey(Student_Task, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comments_student

Paso 20: Creamos la migracion
python manage.py makemigrations feedback  

Paso 21: Creamos el archivo de migraciones
python manage.py migrate feedback

Paso 22 Ir al archivo admin.py y registrar los modelos.
from django.contrib import admin
from models import Teacher
from models import Student
from models import Task
from models import Student_Task
from models import Comments

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Student_Task)
admin.site.register(Comments)


Paso 23: Volvemos a correr el servidor para ver los cambios
python manage.py runserver 

Paso 24: Configurar la zona horaria modificando el archivo settings.py
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "es-mx"
TIME_ZONE = "America/Mexico_City"
USE_I18N = True
USE_TZ = True



