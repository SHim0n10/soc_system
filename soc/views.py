from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by("dostupnost", "id")
    konzultanti = Ucitel.objects.all().order_by("priezvisko")
    studenti = Student.objects.all().order_by("priezvisko")
    odbory = Odbor.objects.all().order_by("nazov")

    return render(request, "soc/index.html", {"temy":temy, "konzultanti":konzultanti, "studenti":studenti, "odbory":odbory})

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

def filter_temy(request):
    nazov_query = request.GET.get('nazov', '')
    popis_query = request.GET.get('popis', '')
    konzultant_query = request.GET.get('konzultant', '')
    student_query = request.GET.get('student', '')
    odbor_query = request.GET.get('odbor', '')
    konzultacie_query = request.GET.get('konzultacie', '')

    temy = Tema.objects.all()

    if nazov_query:
        temy = temy.filter(nazov__icontains=nazov_query)
    if popis_query:
        temy = temy.filter(popis__icontains=popis_query)
    if konzultant_query:
        temy = temy.filter(konzultant=konzultant_query)
    if student_query:
        temy = temy.filter(student=student_query)
    if odbor_query:
        temy = temy.filter(odbor=odbor_query)
    if konzultacie_query:
        temy = temy.filter(konzultacie__icontains=konzultacie_query)

    results = []
    for tema in temy:
        results.append({
            'id': tema.id,
            'nazov': tema.nazov,
            'popis': tema.popis,
            'konzultant': str(tema.konzultant),  # Convert to string
            'dostupnost': tema.dostupnost.nazov,
            'student': str(tema.student) if tema.student else '----',  # Convert to string
            'odbor': str(tema.odbor),
            'konzultacie': tema.konzultacie
        })
    return JsonResponse(results, safe=False)

