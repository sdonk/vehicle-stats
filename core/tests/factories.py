import factory

from core import models


class VehicleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Vehicle
        django_get_or_create = ('registration',)

    name = factory.Sequence(lambda n: "Vehicle %03d" % n)
    registration = factory.Sequence(lambda n: "%03d" % n)
    year_manufactured = '2018'
    cost_of_purchase = 1


class FuelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Fuel

    vehicle = factory.SubFactory(VehicleFactory)
    cost = 20.23
