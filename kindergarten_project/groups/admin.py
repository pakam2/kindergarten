from django.contrib import admin
from groups.models import Group, Child, GroupSchedule


@admin.register(Group)
class AdminGroup(admin.ModelAdmin):

    #Actions
    def change_to_older(self, request, queryset):
        rows_to_update = queryset.update(type_of_group = 'O')
        if rows_to_update == 1:
            message_bit = "One group"
        else:
            message_bit = "{} groups".format(rows_to_update)
        self.message_user(request, "{} changed to 'Older'".format(message_bit))


    def change_to_younger(self, request, queryset):
        rows_to_update = queryset.update(type_of_group = 'Y')
        if rows_to_update == 1:
            message_bit = 'One group'
        else:
            message_bit = '{} groups'.format(rows_to_update)
        self.message_user(request, "{} changed to 'Younger'".format(message_bit))

    actions =['change_to_older', 'change_to_younger']

    #Short description of actions displayed on site (name of acton)
    change_to_older.short_description = "Changed the group type to 'Older'"
    change_to_younger.short_description = "Changed the group type to 'Younger'"

    #Formating the name of fields
    def get_group_name(self):
        return 'Group name "{} {}"'.format(self.group_name[0:5], self.group_name[5:])

    list_display = (get_group_name, 'type_of_group')



@admin.register(Child)
class AdminChild(admin.ModelAdmin):


    #Actions
    def change_to_group_one(self, request, queryset):
        rows_to_update = queryset.update(group_id = 1)
        if rows_to_update == 1:
            message_bit = "One child"
        else:
            message_bit = "{} childs".format(rows_to_update)
        self.message_user(request, "{} group changed to 'Group 1'".format(message_bit))

    def change_to_group_two(self, request, queryset):
        rows_to_update = queryset.update(group_id = 2)
        if rows_to_update == 2:
            message_bit = "One child"
        else:
            message_bit = "{} childs".format(rows_to_update)
        self.message_user(request, "{} group changed to 'Group 1'".format(message_bit))


    #Short description of actions displayed on site (name of action)
    change_to_group_one.short_description = "Change the group to 'Group 1'"
    change_to_group_two.short_description = "Change the group to 'Group 2'"

    actions = ['change_to_group_one', 'change_to_group_two']

    #Formating the name of fields

    list_display = ['name', 'parent', 'group']
