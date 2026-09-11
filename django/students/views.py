from django.shortcuts import render, redirect, get_object_or_404
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
