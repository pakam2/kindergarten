from django.conf.urls import url

from .views import ParentDetailView

urlpatterns = [
    url (r'^(?P<first_name>[\w.@+-]+)/$', ParentDetailView.as_view(), name='detail'),
]