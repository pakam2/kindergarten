from django.db import models


GROUP = (('Y', 'Younger'),
         ('O','Older'))

class Child(models.Model):
    name = models.CharField(max_length=255)
    #picture = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    # parent = models.ManyToMany(Parent, related_name='parent_of_child') // FK u parenta?

    def __str__(self):
        return self.name


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    type_of_group = models.CharField(max_length=1, choices=GROUP)
#	child = models.ForeignKey(Child)
    #teachers = models.ManyToManyField(Teacher, related_name='teacher_of_group') // trzeba zaimportować z accounts

    def __str__(self):
        return self.group_name
