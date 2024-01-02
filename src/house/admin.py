from django.contrib import admin

# Register your models here.


from .models import House


class HouseAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created_on']


admin.site.register(House, HouseAdmin)
