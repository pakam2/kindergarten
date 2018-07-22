from django.conf import settings
from django.db import models
from groups.models import Child, Group
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



#Extending User model with two fields

class Parent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    child = models.ManyToManyField(Child, related_name="childs_parent")

#Everytime a save event occurs a model is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Parent.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.parent.save()





class Guardian(models.Model):

    user = models.OneToOneField(User)
    parent = models.ManyToManyField(Parent, related_name='teacher') # czy potrzebne?
    group = models.ManyToManyField(Group, related_name='group')

    def __str__(self):
        return self.user
