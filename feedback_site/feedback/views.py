from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib import messages


# Create your views here.
def home(request):
    teacherslistados = Teacher.objects.all()
    return render(request, "gestionteacher.html", {"teachers": teacherslistados})


def registrarMaestros(request):
    name = request.POST.get("txtName")
    surnames = request.POST.get("txtSurnames")
    email = request.POST.get("txtEmail")
    career = request.POST.get("txtCareer")
    pub_date = request.POST.get("txtPub_date")
    teacher = Teacher.objects.create(
        name=name, surnames=surnames, email=email, career=career, pub_date=pub_date
    )
    return redirect("/")


def edicionTeacher(request, name):
    teacher = Teacher.objects.get(name=name)
    return render(request, "editarTeacher.html", {"teacher": teacher})


def editarTeacher(request):
    name = request.POST.get("txtName")
    surnames = request.POST.get("txtSurnames")
    email = request.POST.get("txtEmail")
    career = request.POST.get("txtCareer")
    pub_date = request.POST.get("txtPub_date")

    teacher = Teacher.objects.get(name=name)
    teacher.name = name
    teacher.surnames = surnames
    teacher.email = email
    teacher.career = career
    teacher.pub_date = pub_date
    teacher.save()

    messages.success(request, "¡Teacher actualizado!")

    return redirect("/")


def eliminarTeacher(request, name):
    teacher = Teacher.objects.get(name=name)
    teacher.delete()

    messages.success(request, "¡Teacher eliminado!")

    return redirect("/")
