from django.conf.urls import url

from .views import ParentDetailView

urlpatterns = [
    url (r'^(?P<username>[\w.@+-]+)/$', ParentDetailView.as_view(), name='detail'),
]