from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("galeria", views.galeria),
    path("dodaj", views.dodaj),
    path("usun/<int:id>", views.usun, name="usun"),
    path("edytuj/<int:id>", views.edytuj, name="edytuj")

]
