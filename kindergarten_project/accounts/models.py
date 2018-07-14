from django.db import models
from groups.models import Child
from django.contrib.auth.models import User
#User = settings.AUTH_USER_MODEL


class Parent(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    child = models.ManyToManyField(Child, related_name="childs_parent")
    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    child = models.ForeignKey(Child)



class Guardian(models.Model):
    user = models.OneToOneField(User)
    parent = models.ManyToManyField(Parent, related_name='guardian')
