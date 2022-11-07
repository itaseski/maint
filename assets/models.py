from enum import unique
from django.db import models


class Vehicle(models.Model):
    """
    VIN - according to ISO 3779Vehicle
    """
    vin = models.CharField ("Vehicle identification number (VIN)", max_length=17, unique=True)
    assembly_date = models.DateField(auto_now=False, auto_now_add=False)
    entry_into_service = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
   

    def __str__(self):
        return self.vin

    def wmi(self):
        """
        WMI - Manufacturer Identifier

        Managed by SAE
        """
        return self.vin[0:3]

    def vds(self):
        """
        VDS - Vehicle Attributes

        Managed by manufacturer        
        """
        return self.vin[3:8]

    def wheel_configuration(self):
        """
        VDS - Vehicle Attributes

        Managed by manufacturer        
        """
        return self.vin[4:7]

    def check_digit(self):
        """
        Check Digit

        Calculated value        
        """
        return self.vin[8]

    def model_year(self):
        """
        Model Year

        Managed by manufacturer        
        """
        return self.vin[9]

    def model_year(self):
        """
        Plant Code

        Managed by manufacturer        
        """
        return self.vin[10]



class General(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    assembly_level = models.CharField(max_length=24, default='Комплетно изграден')
    production_class = models.CharField(max_length=24, default='Камион')
    development_level = models.CharField(max_length=2, default='5')
    front_wheel_drive = models.CharField(max_length=6, default='Нема')
    axle_distance = models.CharField(max_length=14, default='3700mm')
    chassis_width = models.CharField(max_length=18, default='2550mm')
    chassis_adaptation = models.CharField(max_length=64, default='A, има водечка спојка која овозможува оштро свртување')
    # truck_model = models.CharField(max_length=2, default='R')
    transport_type = models.CharField(max_length=2, default='L')
    duty_class = models.CharField(max_length=2, default='M')
    chassis_height = models.CharField(max_length=24, default='N, Нормална')
    plate_language = models.CharField(max_length=12, default='English')
    axle_weight_front_technical = models.CharField(max_length=12, default='7500kg')
    axle_load_rear_technical = models.CharField(max_length=12, default='115000kg')
    total_weight = models.CharField(max_length=12, default='19000kg')
    preparation_for_toll_collect = models.CharField(max_length=6, default='Има')

    def __str__(self):
        return self.vehicle.vin

    def wheel_configuration(self):
        return self.vehicle.vin[4:7]
    
    def truck_model(self):
        return self.vehicle.vin[3]

    class Meta:
        verbose_name_plural = "General"

   

    

class LicencePlate(models.Model):
    '''Licence Plate'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    code = models.CharField(max_length=8, unique=True)
    is_valid = models.BooleanField()
    validity = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.vehicle.vin


class EngineInfo(models.Model):
    '''Engine'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    stroke_volume = models.CharField(max_length=2, default="13")
    power_code = models.CharField(max_length=5, default="410hp")
    type_vehicle = models.CharField(max_length=14, default="DC13 115/410hp")
    type_symbol = models.CharField(max_length=12, default="DC13 115 L01")
    serial_no = models.CharField(max_length=7)
    cylinder_block_generation = models.CharField(max_length=1, default="2")
    speed_limit_with_low_oil_presure = models.CharField(max_length=14, default='Without')
    egr_system = models.CharField(max_length=14, default='Without')
    egr_cooling = models.CharField(max_length=14, default='Not valid')
    emmission_level = models.CharField(max_length=14, default='Euro 6')
    management_system = models.CharField(max_length=2, default='S8')
    nox_control = models.CharField(max_length=14, default='With')
    torque_reduction_nox_control = models.CharField(max_length=14, default='With')
    power_take_of_ED = models.CharField(max_length=24, default='Prepared')
    power_take_of_ED_electical_preparation = models.CharField(max_length=24, default='Without')
    power_take_of_ED_control = models.CharField(max_length=14, default='Without')
    turbocharger_duty_class = models.CharField(max_length=14, default='Специјална')
    precleaner_air_intake = models.CharField(max_length=14, default='Without')
    air_intake = models.CharField(max_length=18, default='Front, normal')
    air_cleaner_engine_fire_resistant = models.CharField(max_length=14, default='Without')
    air_cleaner_safety_filter = models.CharField(max_length=14, default='Without')
    air_cleaner_engine_paper_area = models.CharField(max_length=14, default='13m²')
    air_intake_throttle_engine = models.CharField(max_length=14, default='With')
    air_intake_throttle_control = models.CharField(max_length=14, default='Electronic')
    air_filter_clogged_indicator = models.CharField(max_length=14, default='Electronic')
    noise_dampering = models.CharField(max_length=64, default='80 dBA acc to 70/157/EEC')
    noise_encapsulation_engine = models.CharField(max_length=18, default='With absorbents')
    crankcase_ventilation_type = models.CharField(max_length=14, default='Open')
    crankcase_ventilation_antitreeze = models.CharField(max_length=14, default='Without')
    oil_level_sensor_engine = models.CharField(max_length=14, default='Without')
    oil_level_sensor_monitoring = models.CharField(max_length=14, default='Without')
    oil_sump_material = models.CharField(max_length=14, default='Пластика')

    def __str__(self):
        return self.vehicle.vin

class FrontAxle(models.Model):
    '''Front Axle'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type = models.CharField(max_length=12, default="AM740")

    def __str__(self):
        return self.vehicle.vin   

class RearAxle(models.Model):
    '''Rear Axle'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type = models.CharField(max_length=12, default="ADA1100")
    oil_filter = models.CharField(max_length=12, default="Има")
    gear_first = models.CharField(max_length=12, default="R780")
    serial_no = models.CharField(max_length=12, default="2418002")
    gear_ratio = models.CharField(max_length=12, default="3.08")
    diferential_block = models.CharField(max_length=12, default="Има")
    hub_reduction = models.CharField(max_length=12, default="Нема")
    tag_axle_preparation = models.CharField(max_length=12, default="Нема")

    def __str__(self):
        return self.vehicle.vin   


class EngineControl(models.Model):
    '''Engine'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    speed_limiter = models.CharField(max_length=12, default="Има")
    speed_limitаtion = models.CharField(max_length=12, default="85km/h")
    speed_limit_second = models.CharField(max_length=12, default="Нема")
    speed_limit_third = models.CharField(max_length=12, default="Нема")

    def __str__(self):
        return self.vehicle.vin

class ComplementaryEquipment(models.Model):
    '''Engine'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fifth_wheel = models.CharField(max_length=24, default="JOST JSK37C-Z 150")
    fifth_wheel_position = models.CharField(max_length=12, default="660")
    fifth_wheel_category = models.CharField(max_length=32, default="Fixed, plate-mounted")
    fifth_wheel_mounting_plate = models.CharField(max_length=24, default="40mm Dmax:152kN")
    catwalk = models.CharField(max_length=24, default="Единечна")
    bracket_front_mounted_equipment = models.CharField(max_length=24, default="Нема")
    acl_aut_chassis_lubrication = models.CharField('ACL, automatic chassis lubrication', max_length=24, default="Нема")
    dimension_ja_bep_lo2o = models.CharField('Dimesion JA/BEP L020', max_length=24, default="775")
    trailer_electric_connector = models.CharField(max_length=24, default="1x15 pole")
    trailer_connector_type = models.CharField(max_length=24, default="High")
    side_skirts = models.CharField(max_length=36, default="Without")
    resque_equip_except_fire_ex = models.CharField(max_length=24, default="With")
    hose_tyre_inflation = models.CharField(max_length=24, default="20")
    spare_wheel_carrier = models.CharField(max_length=24, default="Without")
    fire_extinguisher = models.CharField(max_length=24, default="1 x 2kg")

    def __str__(self):
        return self.vehicle.vin   



