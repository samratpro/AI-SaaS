from django.contrib import admin
from .models import *
# Register your models here.

class ApiListAdmin(admin.ModelAdmin):
    readonly_fields = ('filled_quota',)  # Add the field you want to make read-only

admin.site.register(ApiList, ApiListAdmin)



admin.site.register(Logo)
admin.site.register(Website_List)
admin.site.register(Youtube_api)


