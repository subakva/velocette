from django.contrib import admin

from velocette.accounts.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_zone')

admin.site.register(Profile, ProfileAdmin)
