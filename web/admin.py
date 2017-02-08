from django.contrib import admin
import models

class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ['visitor']


admin.site.register(models.Message, admin_class=MessageAdmin)
