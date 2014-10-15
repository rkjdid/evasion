from evasion import models
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ['visitor']


admin.site.register(models.Message, admin_class=MessageAdmin)
