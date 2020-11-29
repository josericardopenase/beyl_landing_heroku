from django.contrib import admin
from django.urls import path, re_path
from .views import home, plans, team, features, faq, sendEmail, influencer, succed, error

urlpatterns = [
    path('', home, name="home"),
    path('team/', team, name="team" ),
    path('features/', features, name="features" ),
    path('sendEmail/', sendEmail, name='sendEmail'),
    path('influencers/', influencer, name='influencer'),
    path('succeed/', succed, name='succeed' ),
    path('error/', error, name='error' )
    #path('faq/', faq, name="faq" )
    
]
"""     path('planes/', plans, name="plans"),
    path('planes/<str:plan>/', plans, name="anual_plans"), """