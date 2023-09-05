from django.contrib import admin
from .models import Teacher, Student, Task, Student_Task, Comments


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Student_Task)
admin.site.register(Comments)
