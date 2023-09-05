from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("registrarMaestros/", views.registrarMaestros),
    path("edicionTeacher/<name>", views.edicionTeacher),
    path("editarTeacher/", views.editarTeacher),
    path("eliminarTeacher/<name>", views.eliminarTeacher),
]
