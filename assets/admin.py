from django.contrib import admin

from .models import Vehicle, General, LicencePlate, EngineInfo, FrontAxle, RearAxle, EngineControl, ComplementaryEquipment

class LicencePlateInline(admin.StackedInline):
    model = LicencePlate
    extra = 1

class VehicleAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Vehicle idetification number ISO 3779:2009',               {'fields': ['vin']}),
        ('Production information', {'fields': ['assembly_date', 'entry_into_service']}),
        ('Vehicle Image', {'fields': ['image']}),
    ]
    inlines = [LicencePlateInline]

admin.site.register(Vehicle, VehicleAdmin)

admin.site.register(LicencePlate)

class EngineInfoAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'type_vehicle')

admin.site.register(EngineInfo, EngineInfoAdmin)


class FrontAxleAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'type')

admin.site.register(FrontAxle, FrontAxleAdmin)


class RearAxleAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'serial_no', 'gear_ratio')

admin.site.register(RearAxle, RearAxleAdmin)

class EngineControlAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'speed_limitаtion')

admin.site.register(EngineControl, EngineControlAdmin)


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


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'duty_class')

admin.site.register(General, GeneralAdmin)