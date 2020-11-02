from django.shortcuts import render
from .models import Plan, TeamMember, Feature

# Create your views here.
def home(request):


    return render(request, 'pages/home.html')



def plans(request, plan = ""):

    context = {
        'plans' : Plan.objects.all().prefetch_related('features'),
        'plan' : plan
    }

    return render(request, 'pages/plans.html', context)

def team(request):
    
    context = {
        'team_members' : TeamMember.objects.all().order_by('order')
    }

    return render(request, 'pages/team.html', context)


def features(request):
    
    context = {
        'features' : Feature.objects.all().order_by('order')
    }


    return render(request, 'pages/features.html', context)


def faq(request):

    return render(request, 'pages/faq.html')

