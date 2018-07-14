from django.db import models

User = settings.AUTH_USER_MODEL


class Parent(models.Model):
    user = models.OneToOneField(User)
    # child = models.ForeignKey()
    pass


class Teacher(models.Model):
    user = models.OneToOneField(User)
