from django.urls import path
from . import views

app_name = "dbApp"

urlpatterns = [
    path('', views.index, name="index"),
]