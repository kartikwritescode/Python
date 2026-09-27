
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


# CREATE
def student_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll_no = request.POST.get("roll_no")
        email = request.POST.get("email")
        course = request.POST.get("course")
        age = request.POST.get("age")

        Student.objects.create(
            name=name,
            roll_no=roll_no,
            email=email,
            course=course,
            age=age
        )

        return redirect("student_list")

    return render(request, "students/student_create.html")


# READ - All students
def student_list(request):
    students = Student.objects.all()

    context = {
        "students": students
    }

    return render(
        request,
        "students/student_list.html",
        context
    )


# READ - Single student
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_detail.html",
        context
    )


# UPDATE
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.roll_no = request.POST.get("roll_no")
        student.email = request.POST.get("email")
        student.course = request.POST.get("course")
        student.age = request.POST.get("age")

        student.save()

        return redirect("student_list")

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_update.html",
        context
    )


# DELETE
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_delete.html",
        context
    )