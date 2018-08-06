from django.conf.urls import url

from .views import ParentDisplayAPIView

urlpatterns = [
    url(r'^(?P<pk>(\d)+)/parent/$', ParentDisplayAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>(\d)+)/user/$', ParentDisplayAPIView.as_view(), name='detail'),
]