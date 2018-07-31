from django.conf.urls import url

from .views import (
    ChildDisplayAPIView,
    ChildCreateAPIView,
    GroupDisplayAPIView,
    GroupCreateAPIView,
)

urlpatterns = [
    url(r'^child-list/$', ChildDisplayAPIView.as_view(), name='child-list'),
    url(r'^child-create/$', ChildCreateAPIView.as_view(), name='child-create'),
    url(r'^group-list/$', GroupDisplayAPIView.as_view(), name='group-list'),
    url(r'^group-create/$', GroupCreateAPIView.as_view(), name='group-create'),

]