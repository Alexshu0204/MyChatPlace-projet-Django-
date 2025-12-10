from django.urls import path
from . import views # Le point situé sur cette ligne permet de regarder dans le dossier courant (base) et de retrouver le fichier de l'importation 

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room")
]