from django.db import models
from groups.models import Child
User = settings.AUTH_USER_MODEL


class Parent(models.Model):

    first_name = models.CharField(max_lenght=255)
    last_name = models.CharField(max_lenght)
    child = models.ManyToMany(Child, related_name="childs_parent")
    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    child = models.ForeignKey(Child)

class Guardian(models.Model):
    user = models.OneToOneField(User)
    parent = models.ManyToManyField(Parent, related_name='guardian')
