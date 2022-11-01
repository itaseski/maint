from django.contrib import admin

from .models import Vehicle, LicencePlate, EngineInfo, FrontAxle, EngineControl, ComplementaryEquipment

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

class FrontAxleAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'front_axle_type')

admin.site.register(FrontAxle, FrontAxleAdmin)

class ComplementaryEquipmentAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'fifth_wheel')
    fieldsets = [
        ('Vehicle VIN',               {'fields': ['vehicle']}),
        ('Fift wheel',               {'fields': ['fifth_wheel', 'fifth_wheel_position', 'fifth_wheel_category', 'fifth_wheel_mounting_plate']}),
        ('Rest', {'fields': ['catwalk', 'bracket_front_mounted_equipment', 'acl_aut_chassis_lubrication', 'dimension_ja_bep_lo2o']}),
        ('Trailer connector', {'fields': ['trailer_electric_connector', 'trailer_connector_type']}),
        ('Resr2', {'fields': ['side_skirts', 'resque_equip_except_fire_ex','hose_tyre_inflation','spare_wheel_carrier', 'fire_extinguisher']}),
    ]

admin.site.register(ComplementaryEquipment, ComplementaryEquipmentAdmin)
