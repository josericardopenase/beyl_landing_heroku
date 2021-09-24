from django import forms

class SendEmailForm(forms.Form):

    name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(required=True)
    rssc = forms.CharField(max_length=200, required=False)
    social_media = forms.CharField(max_length=50, required=False)
    confirm_privacy = forms.BooleanField()
    has_used_other_tool = forms.CharField(required=False)

class ConseguirEntrada(forms.Form):

    nombre = forms.CharField(max_length=200, required=False)
    apellidos = forms.CharField(max_length=200, required=False)
    horario = forms.CharField(max_length=200, required=False)
    edad = forms.IntegerField(required=False)
    email = forms.EmailField(required=True)