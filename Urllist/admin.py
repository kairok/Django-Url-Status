from django.contrib import admin
from  Urllist.models import Links


class LinksAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("creater", "url", "date")

    #def invited_user(self, obj):
    #    return "\n".join([user.username for user in obj.invited.all()])



admin.site.register(Links, LinksAdmin)