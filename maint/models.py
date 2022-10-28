from enum import unique
from django.db import models


class Vehicle(models.Model):
    """
    VIN - according to ISO 3779Vehicle
    """
    vin = models.CharField ("Vehicle identification number (VIN)", max_length=17, unique=True)
    assembly_date = models.DateField(auto_now=False, auto_now_add=False)
    entry_into_service = models.DateField(auto_now=False, auto_now_add=False)
   

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

    def model_year(self):
        """
        Sequential Number

        Managed by manufacturer        
        """
        return self.vin[11:]


class LicencePlate(models.Model):
    '''Licence Plate'''
    code = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    code_text = models.CharField(max_length=8, unique=True)
    is_valid = models.BooleanField()
    validity = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.code_text


class EngineInfo(models.Model):
    '''Engine'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    engine_stroke_volume = models.CharField(max_length=2, default="13")
    power_code = models.CharField(max_length=5, default="410hp")
    engine_type_vehicle = models.CharField(max_length=14, default="DC13 115/410hp")
    engine_type_symbol = models.CharField(max_length=12, default="DC13 115 L01")
    engine_serial_no = models.CharField(max_length=7)
    cylinder_block_generation = models.CharField(max_length=1, default="2")
    engine_speed_limit_with_low_oil_presure = models.CharField(max_length=14, default='Without')
    egr_system = models.CharField(max_length=14, default='Without')
    egr_cooling = models.CharField(max_length=14, default='Not valid')
    emmission_level = models.CharField(max_length=14, default='Euro 6')
    engine_management_system = models.CharField(max_length=2, default='S8')
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
    front_axle_type = models.CharField(max_length=12, default="AM740")

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





