from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    surnames = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    carer = models.CharField(max_length=200)
    semester = models.IntegerField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    datetimelimit = models.DateTimeField("date published")
    points = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title


class Student_Task(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to="files/%Y/%m/%d/")
    pub_date = models.DateTimeField("date published")
    qualification = models.CharField(max_length=200)
    comments_teacher = models.CharField(max_length=1000)

    def __str__(self):
        return self.task.title


class Comments(models.Model):
    student_task = models.ForeignKey(Student_Task, on_delete=models.CASCADE)
    comments_student = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        texto = "{0} - {1} - {2}"
        return texto.format(
            self.student_task.task.title, self.student_task.student.name, self.pub_date
        )
