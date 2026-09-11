
import os
import subprocess
import sys
from pathlib import Path

PROJECT = "myproject"
APP = "students"


def run(command):
    print(f"\n>>> {command}")
    subprocess.run(command, shell=True, check=True)


# --------------------------------------------------
# 1. Create Django project
# --------------------------------------------------

if not Path("manage.py").exists():
    run(f"django-admin startproject {PROJECT} .")

# Create app
if not Path(APP).exists():
    run(f"python manage.py startapp {APP}")


# --------------------------------------------------
# 2. Modify settings.py
# --------------------------------------------------

settings_file = Path(PROJECT) / "settings.py"
settings = settings_file.read_text()

if f"'{APP}'" not in settings:
    settings = settings.replace(
        "INSTALLED_APPS = [",
        f"INSTALLED_APPS = [\n    '{APP}',"
    )

settings_file.write_text(settings)


# --------------------------------------------------
# 3. Create Model
# --------------------------------------------------

models = '''from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
'''

Path(APP, "models.py").write_text(models)


# --------------------------------------------------
# 4. Create Views
# --------------------------------------------------

views = '''from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


# CREATE
def create_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        course = request.POST["course"]

        Student.objects.create(
            name=name,
            age=age,
            course=course
        )

        return redirect("student_list")

    return render(request, "create_student.html")


# READ
def student_list(request):
    students = Student.objects.all()

    return render(request, "student_list.html", {
        "students": students
    })


# UPDATE
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.age = request.POST["age"]
        student.course = request.POST["course"]

        student.save()

        return redirect("student_list")

    return render(request, "update_student.html", {
        "student": student
    })


# DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "delete_student.html", {
        "student": student
    })
'''

Path(APP, "views.py").write_text(views)


# --------------------------------------------------
# 5. Create App URLs
# --------------------------------------------------

app_urls = '''from django.urls import path
from . import views


urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("create/", views.create_student, name="create_student"),
    path("update/<int:id>/", views.update_student, name="update_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
]
'''

Path(APP, "urls.py").write_text(app_urls)


# --------------------------------------------------
# 6. Modify Project URLs
# --------------------------------------------------

project_urls = '''from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
]
'''

Path(PROJECT, "urls.py").write_text(project_urls)


# --------------------------------------------------
# 7. Create Templates
# --------------------------------------------------

templates = Path(APP) / "templates"
templates.mkdir(parents=True, exist_ok=True)


# CREATE TEMPLATE
create_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Add Student</title>
</head>
<body>

<h1>Add Student</h1>

<form method="POST">
    {% csrf_token %}

    <input type="text"
           name="name"
           placeholder="Name"
           required>

    <input type="number"
           name="age"
           placeholder="Age"
           required>

    <input type="text"
           name="course"
           placeholder="Course"
           required>

    <button type="submit">
        Create Student
    </button>
</form>

<br>

<a href="{% url 'student_list' %}">
    Back to Students
</a>

</body>
</html>
'''

(templates / "create_student.html").write_text(create_html)


# READ TEMPLATE
list_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Students</title>
</head>
<body>

<h1>Students</h1>

<a href="{% url 'create_student' %}">
    Add Student
</a>

<hr>

{% for student in students %}

<div>

    <strong>{{ student.name }}</strong>

    <br>

    Age: {{ student.age }}

    <br>

    Course: {{ student.course }}

    <br>

    <a href="{% url 'update_student' student.id %}">
        Edit
    </a>

    <a href="{% url 'delete_student' student.id %}">
        Delete
    </a>

</div>

<hr>

{% empty %}

<p>No students found.</p>

{% endfor %}

</body>
</html>
'''

(templates / "student_list.html").write_text(list_html)


# UPDATE TEMPLATE
update_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Update Student</title>
</head>
<body>

<h1>Update Student</h1>

<form method="POST">

    {% csrf_token %}

    <input type="text"
           name="name"
           value="{{ student.name }}"
           required>

    <input type="number"
           name="age"
           value="{{ student.age }}"
           required>

    <input type="text"
           name="course"
           value="{{ student.course }}"
           required>

    <button type="submit">
        Update Student
    </button>

</form>

<br>

<a href="{% url 'student_list' %}">
    Back
</a>

</body>
</html>
'''

(templates / "update_student.html").write_text(update_html)


# DELETE TEMPLATE
delete_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Delete Student</title>
</head>
<body>

<h1>Delete Student</h1>

<p>
    Are you sure you want to delete
    <strong>{{ student.name }}</strong>?
</p>

<form method="POST">

    {% csrf_token %}

    <button type="submit">
        Yes, Delete
    </button>

</form>

<br>

<a href="{% url 'student_list' %}">
    Cancel
</a>

</body>
</html>
'''

(templates / "delete_student.html").write_text(delete_html)


# --------------------------------------------------
# 8. Make Migrations
# --------------------------------------------------

run("python manage.py makemigrations")
run("python manage.py migrate")


# --------------------------------------------------
# DONE
# --------------------------------------------------

print("\n" + "=" * 50)
print("DJANGO CRUD PROJECT CREATED SUCCESSFULLY!")
print("=" * 50)

print("\nRun the server:")
print("    python manage.py runserver")

print("\nThen open:")
print("    http://127.0.0.1:8000/students/")

print("\nCRUD URLs:")
print("    READ   -> /students/")
print("    CREATE -> /students/create/")
print("    UPDATE -> /students/update/<id>/")
print("    DELETE -> /students/delete/<id>/")
