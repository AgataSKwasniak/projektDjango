from django.shortcuts import render, redirect, get_object_or_404
from .models import Kontakt
from .forms import KontaktForm

# Create your views here.
def home(request):
    listaKontaktow = Kontakt.objects.all()
    return render(request, "home.html", {"dane":listaKontaktow})

def galeria(request):
    return render(request, "galeria.html")

def dodaj(request):

    if request.method == "POST":
        ob = KontaktForm(request.POST)
        ob.save()
        return redirect("home")
    else:
        ob = KontaktForm()
        return render(request, "dodaj.html", {"form":ob})

def usun(request, id):
    Kontakt.objects.filter(pk=id).delete()
    return redirect("home")

def edytuj(request, id):
    kontakt = get_object_or_404(Kontakt, pk=id)

    if request.method == "POST":
        ob = KontaktForm(request.POST, instance=kontakt)
        ob.save()
        return redirect("home")
    else:
        ob = KontaktForm(instance=kontakt)
        return render(request, "edytuj.html", {"form": ob})

