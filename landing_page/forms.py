from django import forms

class SendEmailForm(forms.Form):

    email = forms.EmailField(required=True)
    rssc = forms.CharField(max_length=200, required=False)
    social_media = forms.CharField(max_length=50, required=False)
    confirm_privacy = forms.BooleanField()