from api.models import Server
from api.models import User
from api.models import Ban
from api.models import Pardon
from django.contrib import admin

admin.site.register(Server)
admin.site.register(User)
class BanAdmin(admin.ModelAdmin):
    # ...
    list_display = ('username', 'server', 'banned_by', 'ban_time', 'banned_ip', 'ban_type', 'was_pardoned')
admin.site.register(Ban, BanAdmin)
admin.site.register(Pardon)
