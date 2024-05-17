from django.contrib import admin
from apps.profile_.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'age', 'favorite_genre')


admin.site.register(Profile, ProfileAdmin)
