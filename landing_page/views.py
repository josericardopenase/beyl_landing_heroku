from django.shortcuts import render
from .models import Plan, TeamMember, Feature, Faq
from .forms import SendEmailForm
from .models import Emails
from django.http import HttpResponseRedirect
from django.urls import reverse
from anymail.message import AnymailMessage
from anymail.message import EmailMessage
from django.template.loader import render_to_string

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

        print(request.POST)
        form = SendEmailForm(request.POST)


        if form.is_valid():
            if(Emails.objects.filter(email = form.cleaned_data['email']).first()): 
                return HttpResponseRedirect(reverse('home'))

            email_inst = Emails.objects.create(
                name= form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                rssc= form.cleaned_data['rssc'],
                social_media = form.cleaned_data['social_media'],
                confirm_privacy= form.cleaned_data['confirm_privacy'],
                has_used_other_tool = form.cleaned_data['has_used_other_tool'],
            )

            email_inst.save()


            message = EmailMessage(
                subject="Bienvenido a Beyl",
                to=["Nuevo usuario <" + form.cleaned_data['email'] + ">"],
                 # single recipient...
                # ...multiple to emails would all get the same message
                # (and would all see each other's emails in the "to" header)
            )
            message.template_id = 3   # use this Sendinblue template
            message.from_email = None  # to use the template's default sender
            message.merge_global_data = {
                'name': "Alice",
                'order_no': "12345",
                'ship_date': "May 15",
            }

            message.send()
            
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

def ofertas(request):
    return render(request, 'pages//ofertas.html')


def movil(request):
    return render(request, 'pages/mobile_app.html')

