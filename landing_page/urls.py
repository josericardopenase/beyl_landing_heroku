from django.contrib import admin
from django.urls import path, re_path
from .views import home, plans, movil, team, features, faq, sendEmail, influencer,  succed, error, ofertas

urlpatterns = [
    path('', home, name="home"),
    path('entradas/', team, name="team" ),
    path('conseguir_entrada/', movil, name="movil" ),
]
"""     path('planes/', plans, name="plans"),
    path('planes/<str:plan>/', plans, name="anual_plans"), """