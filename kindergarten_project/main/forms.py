from django import forms


class LoginForm(forms.Form):

    login_field = forms.CharField(max_length=400)
    password = forms.CharField(widget=forms.PasswordInput())
