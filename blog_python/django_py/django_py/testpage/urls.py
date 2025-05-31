from django.urls import path
from .views import index
from .views import neindex

urlpatterns = [
    path("", index, name="index"),
    path("info/", neindex, name="neindex"),

]