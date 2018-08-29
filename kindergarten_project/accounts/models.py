from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from groups.models import Child, Group

User = settings.AUTH_USER_MODEL


#Extending User model with two fields

class Parent(models.Model):
    name_of_parent = models.OneToOneField(User)
    # child = models.ManyToManyField(Child, related_name="childs_parent")

    def __str__(self):
        parent_name = self.name_of_parent
        return f"{parent_name}"


#Everytime a save event occurs a model is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Parent.objects.create(name_of_parent=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.parent.save()


class Guardian(models.Model):
    user = models.OneToOneField(User, related_name='guardian_profile')
    parent = models.ManyToManyField(Parent, related_name='guardian_parent') # czy potrzebne?
    group = models.ManyToManyField(Group, related_name='group')

    def __str__(self):
        return self.user
