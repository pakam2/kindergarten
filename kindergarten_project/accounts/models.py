from django.conf import settings
from django.db import models

from groups.models import Child, Group

User = settings.AUTH_USER_MODEL


class Parent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    child = models.ManyToManyField(Child, related_name="childs_parent", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    # child = models.ForeignKey(Child)

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    user = models.OneToOneField(User)
    parent = models.ManyToManyField(Parent, related_name='teacher') # czy potrzebne?
    group = models.ManyToManyField(Group, related_name='group')

    def __str__(self):
        return self.user
