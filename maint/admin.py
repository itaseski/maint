from django.contrib import admin

from .models import Vehicle, LicencePlate, EngineInfo, FrontAxle, EngineControl

class LicencePlateInline(admin.StackedInline):
    model = LicencePlate
    extra = 1

class EngineInfoInline(admin.StackedInline):
    model = EngineInfo
    extra = 1


class VehicleAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Vehicle idetification number ISO 3779:2009',               {'fields': ['vin']}),
        ('Production information', {'fields': ['assembly_date', 'entry_into_service']}),
    ]
    inlines = [LicencePlateInline]

admin.site.register(Vehicle, VehicleAdmin)

admin.site.register(LicencePlate)

admin.site.register(EngineInfo)

admin.site.register(EngineControl)

admin.site.register(FrontAxle)
