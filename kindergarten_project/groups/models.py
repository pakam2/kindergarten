from django.conf import settings
from django.db import models



GROUP = (('Y', 'Younger'),
         ('O','Older'))

<<<<<<< HEAD
class Group(models.Model):
    group_name = models.CharField(max_length=255)
    type_of_group = models.CharField(max_length=1, choices=GROUP)
    # child = models.ForeignKey(Child)
    # teachers = models.ManyToManyField(Teacher, related_name='teacher_of_group') # trzeba zaimportować z accounts
=======
class Child(models.Model):
    name = models.CharField(max_length=255)
    #picture = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    # parent = models.ManyToMany(Parent, related_name='parent_of_child') // FK u parenta?

    def __str__(self):
        return self.name


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    type_of_group = models.CharField(max_length=1, choices=GROUP)
    child = models.ForeignKey(Child)

#	child = models.ForeignKey(Child)
    #teachers = models.ManyToManyField(Teacher, related_name='teacher_of_group') // trzeba zaimportować z accounts
>>>>>>> 4c6d812c630ebc3efe17f9e4593d7c00e36c19ce

    def __str__(self):
        return self.group_name


class Child(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    group = models.ForeignKey(Group, null=True, blank=True)
    # parent = models.ManyToMany(Parent, related_name='parent_of_child') // FK u parenta?

    def __str__(self):
        return self.name
