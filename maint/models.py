from django.db import models


class Vehicle(models.Model):
    """
    VIN - according to ISO 3779Vehicle
    """
    vin = models.CharField (max_length=17)

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


