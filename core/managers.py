from django.db import models
from django.db.models import Q


class MileageManager(models.Manager):

    def get_all_mileage_objects_by_vehicle(self, vehicle):
        from core.models import Mileage
        return Mileage.objects.filter(
            Q(fuel__vehicle=vehicle) |
            Q(vehicles=vehicle) |
            Q(services__vehicle=vehicle)
        )

    def get_latest_mileage_by_vehicle(self, vehicle):
        from core.models import Mileage
        return Mileage.objects.filter(
            Q(fuel__vehicle=vehicle) |
            Q(vehicles=vehicle) |
            Q(services__vehicle=vehicle)
        ).latest('date')
