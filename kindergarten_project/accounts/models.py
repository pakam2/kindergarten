from django.db import models

User = settings.AUTH_USER_MODEL


class Parent(models.Model):
    user = models.OneToOneField(User)
    # child = models.ForeignKey()
    pass


class Guardian(models.Model):
    user = models.OneToOneField(User)
    parent = models.ManyToManyField(Parent, related_name='guardian')