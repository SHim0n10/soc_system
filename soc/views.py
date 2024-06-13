from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db.models import Count
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by("dostupnost", "id")
    konzultanti = Ucitel.objects.all().order_by("priezvisko")
    studenti = Student.objects.all().order_by("priezvisko")
    odbory = Odbor.objects.all().order_by("nazov")

    return render(request, "soc/index.html", {"temy":temy, "konzultanti":konzultanti, "studenti":studenti, "odbory":odbory})

def vypis_ucitela(request, ucitel):
    try:
        ucitel = Ucitel.objects.get(pk=ucitel)
        temy = Tema.objects.filter(konzultant=ucitel).order_by("dostupnost", "id")
    except:
        ucitel = False
        temy = False

    
    if temy:
        return render(request, "soc/ucitel.html", {"temy":temy, "ucitel":ucitel})
    else:
        return render(request, "soc/ucitel.html", {"ucitel":ucitel})

def vypis_studenta(request, student):
    try:
        student = Student.objects.get(pk=student)
        tema = Tema.objects.filter(student=student)
    except:
        student = False
        tema = False

    if tema:
        return render(request, "soc/student.html", {"tema":tema, "student":student})
    else:
        return render(request, "soc/student.html", {"student":student})

def vypis_temu(request, tema):
    try:
        tema = Tema.objects.get(pk=tema)
    except:
        tema = False

    return render(request, "soc/tema.html", {"tema":tema})

def filter_temy(request):
    nazov_query = request.GET.get('nazov', '')
    popis_query = request.GET.get('popis', '')
    konzultant_query = request.GET.get('konzultant', '')
    student_query = request.GET.get('student', '')
    odbor_query = request.GET.get('odbor', '')
    konzultacie_query = request.GET.get('konzultacie', '')

    temy = Tema.objects.all().order_by("dostupnost", "id")

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

def vypis_stats(request):
    temy = Tema.objects.all().count()
    obsadene = Tema.objects.filter(dostupnost=Dostupnost.objects.get(nazov="obsadené")).count()
    volne = Tema.objects.filter(dostupnost=Dostupnost.objects.get(nazov="voľné")).count()
    cakajuce = Tema.objects.filter(dostupnost=Dostupnost.objects.get(nazov="čakajúce na schválenie")).count()
    ucitelia = Ucitel.objects.all().count()
    ziaci = Student.objects.all().count()
    studenti_s_temamy = Student.objects.annotate(temy=Count('tema'))
    count_studenti = studenti_s_temamy.filter(temy__gt=0).count()
    count_studenti_bez = studenti_s_temamy.filter(temy=0).count()
    ucitelia_s_temamy = Ucitel.objects.annotate(temy=Count('tema'))
    count_ucitelia = ucitelia_s_temamy.filter(temy__gt=0).count()
    count_ucitelia_bez = ucitelia_s_temamy.filter(temy=0).count()
    return render(request, 'soc/statistiky.html', {"temy": temy, "obsadene":obsadene,"cakajuce":cakajuce,"volne":volne,"ziaci":ziaci,"ucitelia":ucitelia,"studenti_s_temamy":count_studenti,"ucitelia_s_temamy":count_ucitelia,"ucitelia_bez_temy":count_ucitelia_bez,"studenti_bez_temy":count_studenti_bez})

def vypis_add_temu(request):
    konzultanti = Ucitel.objects.all().order_by("priezvisko")
    studenti = Student.objects.all().order_by("priezvisko")
    odbory = Odbor.objects.all().order_by("nazov")
    return render(request, "soc/add_tema.html", {"ucitelia":konzultanti, "studenti":studenti, "odbory":odbory})