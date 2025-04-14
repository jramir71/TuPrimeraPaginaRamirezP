from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ejemplo de vista principal
]