import math
from django.db import models

class Testplane(models.Model):
    id = models.AutoField(primary_key=True)
    plane_id = models.IntegerField()
    passenger_capacity = models.IntegerField()

    def fuel_consumption_per_minute(self):
        return math.log(self.plane_id * 0.80) + 0.002 * self.passenger_capacity

    def max_flying_minutes(self):
        fuel_tank_capacity = 200 * self.plane_id
        return fuel_tank_capacity / self.fuel_consumption_per_minute()
    
    def __str__(self):
        return f"Testplane {self.id}"
