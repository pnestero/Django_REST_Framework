from django.urls import path

from lesson_course import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
]
