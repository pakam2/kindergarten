from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    login_field = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'User login', 'class': 'login_input'}), max_length=400)
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'User password', 'class': 'login_input'}))


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(label="", max_length=200, required=False,widget=forms.TextInput(attrs={'placeholder': 'First name'}), help_text="")
    login = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': "Your login"}), required=True)
    last_name = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Last name'}), required=False, help_text="")
    email = forms.EmailField(label="", max_length=400, widget=forms.EmailInput(attrs={'placeholder':'Your email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), help_text="")
    def __init__(self, *args, **kwargs):
        # Override default init from `UserCreationForm` to use email as
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        self.fields['password2'].help_text=''
        self.fields['password2'].label=''

    class Meta:
        model = User
        fields = ['login', 'first_name', 'last_name', 'email', 'password1', 'password2']
