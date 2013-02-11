from django import forms
from django.utils.translation import ugettext_lazy

class LoginForm(forms.Form):
    username = forms.CharField(label = ugettext_lazy("Username"), required = True)
    password = forms.CharField(label = ugettext_lazy("Password"), required = True, widget = forms.PasswordInput())    
