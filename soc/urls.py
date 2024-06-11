from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_tem, name='vypis_tem'),
    path('ucitel/<ucitel>', views.vypis_ucitela, name='ucitel'),
    path('student/<student>', views.vypis_studenta, name='student'),
    path('tema/<tema>', views.vypis_temu, name='tema'),


]