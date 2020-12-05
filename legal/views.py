from django.shortcuts import render

# Create your views here.
def privacidad(request):
    return render(request, 'legal/aviso_legal.html')

def politica(request):
    return render(request, 'legal/politica_privacidad.html')


def cookies(request):
    return render(request, 'legal/cookies.html')