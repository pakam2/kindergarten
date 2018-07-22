from django.conf import settings
from django.db import models

from groups.models import Child, Group

User = settings.AUTH_USER_MODEL


class Parent(models.Model):
    user = models.OneToOneField(User, related_name='parent_profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    child = models.ManyToManyField(Child, related_name="childs_parent")
    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    # child = models.ForeignKey(Child)

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
