from django.forms import ModelForm
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = QueryForm
        feedback = forms.CharField(widget=forms.Textarea)
        captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        fields = "__all__"