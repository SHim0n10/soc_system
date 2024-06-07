from django.shortcuts import render, HttpResponse
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by("dostupnost", "id")

    return render(request, "soc/index.html", {"temy":temy})