from django.shortcuts import render
from .models import Plan, TeamMember, Feature, Faq
from .forms import SendEmailForm
from .models import Emails
from django.http import HttpResponseRedirect
from django.urls import reverse


def plans(request, plan = ""):

    context = {
        'plans' : Plan.objects.all().prefetch_related('features').order_by('order'),
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
    context = {
        'faqs' : Faq.objects.all()
    }
    return render(request, 'pages/faq.html', context)




def sendEmail(request):


    if request.method == 'POST':

        form = SendEmailForm(request.POST)


        if form.is_valid():
            if(Emails.objects.filter(email = form.cleaned_data['email']).first()): 
                return HttpResponseRedirect(reverse('home'))

            email_inst = Emails.objects.create(
                email=form.cleaned_data['email'],
                rssc= form.cleaned_data['rssc'],
                social_media = form.cleaned_data['social_media'],
                confirm_privacy= form.cleaned_data['confirm_privacy']
            )

            email_inst.save()

            return HttpResponseRedirect(reverse('succeed'))

        return HttpResponseRedirect(reverse('error'))


# Create your views here.
def home(request):

    form = SendEmailForm(initial={
        'email' : 'Inserta tu email aqui...'
   })

    return render(request, 'pages/home.html', {'form': form})


def influencer(request):

    return render(request, 'pages/influencers.html')

def succed(request):
    return render(request, 'pages/succed.html')

def error(request):
    return render(request, 'pages/error.html')