import factory
import factory.fuzzy

from core import models


class MileageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Mileage

    miles = factory.fuzzy.FuzzyInteger(1)


class VehicleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Vehicle
        django_get_or_create = ('registration',)

    name = factory.Sequence(lambda n: "Vehicle %03d" % n)
    mileage = factory.SubFactory(MileageFactory)
    registration = factory.Sequence(lambda n: "%03d" % n)
    year_manufactured = '2018'
    cost_of_purchase = 1


class FuelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Fuel

    vehicle = factory.SubFactory(VehicleFactory)
    cost = factory.fuzzy.FuzzyFloat(5, 100)
    mileage = factory.SubFactory(MileageFactory)


class PurchaseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Purchase

    vehicle = factory.SubFactory(VehicleFactory)
    cost = factory.fuzzy.FuzzyFloat(1)
    description = factory.fuzzy.FuzzyText(length=50)


class ServiceFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Service

    mileage = factory.SubFactory(MileageFactory)
    vehicle = factory.SubFactory(VehicleFactory)
    type_of_service = factory.fuzzy.FuzzyChoice(models.Service.TYPES)
    cost = factory.fuzzy.FuzzyFloat(1)
