from django.conf.urls import url

from .views import GroupDisplayAPIView, ChildDisplayAPIView

urlpatterns = [
    url(r'^group-list/$', GroupDisplayAPIView.as_view(), name='group-list'),
    url(r'^child-list/$', ChildDisplayAPIView.as_view(), name='child-list'),
]