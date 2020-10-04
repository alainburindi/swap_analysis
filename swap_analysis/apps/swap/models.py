from django.db import models

from swap_analysis.model import SoftDeleteModel
from swap_analysis.apps.authentication.models import User


class Station(SoftDeleteModel):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)


class Attendant(SoftDeleteModel):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )


class Driver(SoftDeleteModel):
    name = models.CharField(max_length=40)


class Battery(SoftDeleteModel):
    voltage = models.FloatField()


class Motor(SoftDeleteModel):
    color = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, blank=True, null=True)


class Swap(SoftDeleteModel):
    battery_in = models.ForeignKey(
        Battery, on_delete=models.CASCADE, blank=True, null=True)
    battery_out = models.ForeignKey(
        Battery, on_delete=models.CASCADE, related_name="out_swaps")
    station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="in_swaps")
    attendant = models.ForeignKey(Attendant, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    driven_distance = models.FloatField()
    out_state_of_charge = models.FloatField()
    in_state_of_charge = models.FloatField()
    used_energy = models.FloatField()
