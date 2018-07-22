from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from main.forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.

class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form} )

    def post(self, request):
        username = request.POST['login_field']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            return HttpResponse("There is no such user")


class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            login_name = form.cleaned_data['login']
            email_field = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                user = User.objects.create_user(first_name = first_name, last_name=last_name, username=login_name, password=password1, email=email_field)
                user.save()
                return HttpResponse("New user added")
            else:
                return HttpResponse("Passwords aren't identical")
        return HttpResponse('Data is not valid')

class MainView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main.html')
