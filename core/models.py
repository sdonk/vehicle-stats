from datetime import datetime

from django.db import models
from djmoney.models.fields import MoneyField
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Vehicle(TimeStampedModel):
    name = models.CharField(max_length=24)
    registration = models.CharField(max_length=8)
    year_manufactured = models.IntegerField()
    cost_of_purchase = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    purchased_on = models.DateField(default=datetime.utcnow)

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    TYPES = Choices(
        'MOT',
        'Annual service',
        'Insurance',
        'Road tax',
        'Road assistance'
        'Other')

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type_of_service = models.CharField(
        choices=TYPES,
        max_length=50
    )
    miles = models.IntegerField()
    date = models.DateField(default=datetime.utcnow)
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.type_of_service


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
    miles = models.FloatField(blank=True, null=True)
    litres = models.FloatField()
    price_per_litre = MoneyField(
        max_digits=10,
        decimal_places=2,
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


class Mileage(TimeStampedModel):
    date = models.DateField(default=datetime.utcnow)
    miles = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Mileage'

    def __str__(self):
        return self.miles
