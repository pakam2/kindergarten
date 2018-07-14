from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from main.forms import LoginForm

# Create your views here.

class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form} )
