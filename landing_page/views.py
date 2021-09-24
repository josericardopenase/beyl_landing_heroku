from django.shortcuts import render
from .models import Plan, TeamMember, Feature, Faq, Market
from .forms import SendEmailForm, ConseguirEntrada
from .models import Emails
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from anymail.message import AnymailMessage
from anymail.message import EmailMessage
from django.template.loader import render_to_string, get_template
from io import BytesIO
from xhtml2pdf import pisa
import datetime

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def plans(request, plan = ""):

    data = {
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
    }
    pdf = render_to_pdf('pages/entrada.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def team(request):
    
    data = {
        'today': datetime.date.today(), 
        'amount': 39.99,
        'nombre': 'Cooper Mann',
        'edad': 20,
        'mail': 'josericardopenase@gmail.com',
    }
    pdf = render_to_pdf('pages/entrada.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


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

    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = ConseguirEntrada(request.POST)


        if form.is_valid():
            #email_inst.save()

            Market.objects.create(**{
                'horario' :form.cleaned_data['horario'] ,
                'nombre': form.cleaned_data['nombre'],
                'apellidos': form.cleaned_data['apellidos'],
                'edad': form.cleaned_data['edad'],
                'email': form.cleaned_data['email'],
            })

            data = {
                'horario' :form.cleaned_data['horario'] ,
                'today': datetime.date.today(), 
                'amount': 39.99,
                'nombre': form.cleaned_data['nombre'],
                'apellidos': form.cleaned_data['apellidos'],
                'edad': form.cleaned_data['edad'],
                'mail': form.cleaned_data['email'],
            }
            pdf = render_to_pdf('pages/entrada.html', data)
            return HttpResponse(pdf, content_type='application/pdf')
    else:
        return render(request, 'pages/mobile_app.html')

