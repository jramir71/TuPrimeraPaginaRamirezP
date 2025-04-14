from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ejemplo de vista principal
    path('insertar_categoria/', views.insertar_categoria, name='insertar_categoria'),
    path('insertar_autor/', views.insertar_autor, name='insertar_autor'),
    path('insertar_post/', views.insertar_post, name='insertar_post'),
    path('buscar_post/', views.buscar_post, name='buscar_post'),
]