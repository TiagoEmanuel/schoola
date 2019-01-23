
from django.urls import path
from . import views #importa as views do diretorio anterior

urlpatterns = [
    path('', views.index, name ='index')
]
