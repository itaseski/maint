from django.contrib import admin

from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['vin', 'assembly_date', 'entry_into_service']}),
    ]

admin.site.register(Vehicle, VehicleAdmin)
