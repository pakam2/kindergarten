from django.contrib import admin

from accounts.models import Parent, Guardian


admin.site.register(Parent)
admin.site.register(Guardian)
