from django.db import models


class Parent (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField (max_length=255)
    child = models.ManyToManyField(Child, related_name="childs_parent")
    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Teacher (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField (max_length=255)
    group = models.ManyToManyField(Group, related_name="group_of_children")
    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)





