from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

GROUP = (('Y', 'Younger'),
         ('O','Older'))

ACTIVITIES = (
    ('1', 'Activity_1'),
    ('2', 'Activity_2'),
    ('3', 'Activity_3'),
    ('4', 'Activity_4'),
)

LESSON_UNITS = (
    ('1', 'Unit_1'),
    ('2', 'Unit_2'),
    ('3', 'Unit_3'),
    ('4', 'Unit_4'),
    ('5', 'Unit_5'),
    ('6', 'Unit_6'),
    ('7', 'Unit_7'),
    ('8', 'Unit_8'),
)

DAYS = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
)


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    type_of_group = models.CharField(max_length=1, choices=GROUP)
#	child = models.ForeignKey(Child) FK should be in child model so child will be assigned to the group
    #teachers = models.ManyToManyField(Teacher, related_name='teacher_of_group') // trzeba zaimportować z accounts

    def __str__(self):
        return self.group_name


class Child(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    group = models.ForeignKey(Group, null=True, blank=True)
    # parent = models.ManyToMany(Parent, related_name='parent_of_child') // FK u parenta?

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("child-group:child-detail", kwargs={"pk": self.pk})


class GroupSchedule(models.Model):
    group = models.ForeignKey(Group)
    day = models.IntegerField(choices=DAYS)
    activity = models.IntegerField(choices=ACTIVITIES)
    lesson_unit = models.IntegerField(choices=LESSON_UNITS)

    def __str__(self):
        return 'day: {}, activity: {}'.format(self.day, self.activity)


