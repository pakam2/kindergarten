from django.conf.urls import url

from .views import (
    GroupDetailView,
    ChildDetailView,
)

urlpatterns = [
    url(r'^(?P<child_name>[\w.@+-]+)/$', GroupDetailView.as_view(), name='group-detail'),
    url(r'^(?P<group_name>[\w.@+-]+)/$', ChildDetailView.as_view(), name='child-detail'),
]