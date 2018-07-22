from django.conf.urls import url

from .views import (
    GroupDetailView,
    ChildDetailView,
)

urlpatterns = [
    url(r'^(?P<pk>(\d)+)/$', ChildDetailView.as_view(), name='child-detail'),
    url(r'^(?P<group_name>[\w.@+-]+)/$', GroupDetailView.as_view(), name='group-detail'),
]