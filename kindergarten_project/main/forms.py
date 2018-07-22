from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    login_field = forms.CharField(max_length=400)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=200, required=False, help_text="Optional")
    login = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=200, required=False, help_text="Optional")
    email = forms.EmailField(max_length=400)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text="")
    class Meta:
        model = User
        fields = ['login', 'first_name', 'last_name', 'email', 'password1', 'password2']
