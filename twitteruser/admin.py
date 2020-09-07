from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitteruser.models import TwitterUser, Relationship

# Register your models here.

admin.site.register(TwitterUser, UserAdmin)
admin.site.register(Relationship)
