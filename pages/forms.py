import os

from django import forms
from django.core.mail import send_mail
from django.core.validators import EmailValidator

from .models import MyInfo

class ContactForm(forms.Form):
    error_css_class = "lead"
    required_css_class = "required"
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your Name',
            'class': 'form-control',
            }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'email@example.com',
            'class': 'form-control',
            }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            }))

    def send_email(self):
        send_mail(
                "Message from visitor of notabotdev.com",
                self.cleaned_data['message'],
                "@".join(["mailgun", os.environ.get('MAILGUN_DOMAIN', '')],
                [MyInfo.objects.all()[0].email],
                fail_silently=False
                )
