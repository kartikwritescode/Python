from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),

    path(
        "student/<int:id>/",
        views.student_detail,
        name="student_detail"
    ),

    path(
        "create/",
        views.student_create,
        name="student_create"
    ),

    path(
        "update/<int:id>/",
        views.student_update,
        name="student_update"
    ),

    path(
        "delete/<int:id>/",
        views.student_delete,
        name="student_delete"
    ),
]