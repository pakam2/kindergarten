"""kindergarten_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from main.views import LoginView, SignUpView, MainView
from .api import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^profile/', include('accounts.urls', namespace='profile')),
    url(r'^child-group/', include('groups.urls', namespace='child-group')),
    url(r'^api/profile/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^api/groups/', include('groups.api.urls', namespace='groups-api')),
    url(r'^signup/', SignUpView.as_view(), name='signup'),
    url(r'^main/', MainView.as_view(), name='main'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', LoginView.as_view(), name='login-view'),

]
