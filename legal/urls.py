from django.contrib import admin
from django.urls import path, re_path
from .views import privacidad, politica, cookies

urlpatterns = [
    path('aviso_legal/', privacidad, name='aviso_legal'),
    path('privacidad/', politica, name='privacidad'),
    path('cookies/', cookies, name='cookies')
    #path('faq/', faq, name="faq" )
    
]
