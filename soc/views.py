from django.shortcuts import render, HttpResponse
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by("dostupnost", "id")

    return render(request, "soc/index.html", {"temy":temy})

def vypis_ucitela(request, ucitel):
    ucitel = Ucitel.objects.get(pk=ucitel)
    temy = Tema.objects.filter(konzultant=ucitel).order_by("dostupnost", "id")
    
    return render(request, "soc/index.html", {"temy":temy, "ucitel":ucitel})

def vypis_studenta(request, student):
    student = Student.objects.get(pk=student)
    temy = Tema.objects.filter(student=student).order_by("dostupnost", "id")
    
    return render(request, "soc/index.html", {"temy":temy, "student":student})

def vypis_temu(request, tema):
    try:
        tema = Tema.objects.get(pk=tema)
    except:
        tema = False

    return render(request, "soc/index.html", {"tema":tema})