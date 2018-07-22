from django.conf import settings
from django.db import models
<<<<<<< HEAD
from groups.models import Child, Group
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

=======

from groups.models import Child, Group
>>>>>>> d23157a096b7e6ce5c4f723a484ea855ef3703db

User = settings.AUTH_USER_MODEL

<<<<<<< HEAD
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

=======

class Parent(models.Model):
    user = models.OneToOneField(User, related_name='parent_profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    child = models.ManyToManyField(Child, related_name="childs_parent")
    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    # child = models.ForeignKey(Child)
>>>>>>> d23157a096b7e6ce5c4f723a484ea855ef3703db

    def __str__(self):
        return "user - {}, first name - {}".format(self.user, self.first_name)

    def get_absolute_url(self):
        return reverse_lazy("profile:detail", kwargs={"username":self.user.username})


class Guardian(models.Model):
    user = models.OneToOneField(User, related_name='guardian_profile')
    parent = models.ManyToManyField(Parent, related_name='guardian_parent') # czy potrzebne?
    group = models.ManyToManyField(Group, related_name='group')

    def __str__(self):
        return self.user
