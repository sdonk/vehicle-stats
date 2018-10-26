from datetime import datetime

from django.db import models
from djmoney.models.fields import MoneyField
from model_utils import Choices
from model_utils.models import TimeStampedModel

from core.managers import MileageManager


class Vehicle(TimeStampedModel):
    name = models.CharField(max_length=24)
    registration = models.CharField(max_length=8, unique=True)
    year_manufactured = models.PositiveSmallIntegerField()
    cost_of_purchase = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    purchased_on = models.DateField(default=datetime.utcnow)
    mileage = models.ForeignKey(
        'core.Mileage',
        related_name='vehicles',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    TYPES = Choices(
        'MOT',
        'Annual service',
        'Insurance',
        'Road tax',
        'Road assistance',
        'Other')

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type_of_service = models.CharField(
        choices=TYPES,
        max_length=50
    )
    mileage = models.ForeignKey(
        'core.Mileage',
        related_name='services',
        on_delete=models.CASCADE
    )
    date = models.DateField(default=datetime.utcnow)
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.type_of_service[0]


class Purchase(TimeStampedModel):
    date = models.DateField(default=datetime.utcnow)
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    description = models.CharField(max_length=255)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.description


class Fuel(TimeStampedModel):
    date = models.DateField(default=datetime.utcnow)
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    mileage = models.ForeignKey(
        'core.Mileage',
        related_name='fuel',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    litres = models.FloatField(blank=True, null=True)
    price_per_litre = MoneyField(
        max_digits=10,
        decimal_places=3,
        default_currency='GBP',
        blank=True,
        null=True
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Fuel'

    def __str__(self):
        return self.vehicle.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.litres and not self.price_per_litre:
            self.price_per_litre = round(self.cost/self.litres, 3)
        if self.price_per_litre and not self.litres:
            self.litres = round(self.cost/self.price_per_litre, 2)
        return super().save(force_insert=False, force_update=False, using=None,
                            update_fields=None)


class Mileage(TimeStampedModel):
    date = models.DateField(default=datetime.utcnow)
    miles = models.PositiveSmallIntegerField()
    objects = MileageManager()

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Mileage'
