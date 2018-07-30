from django.conf.urls import url

from .views import ParentDisplayAPIView

urlpatterns = [
    url (r'^(?P<pk>(\d)+)/$', ParentDisplayAPIView.as_view(), name='detail'),
]