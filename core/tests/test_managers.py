import pytest

from core import models
from . import factories


@pytest.mark.django_db
def test_get_mileage_all_objects_by_vehicle():
    vehicle = factories.VehicleFactory()
    factories.ServiceFactory(vehicle=vehicle)
    factories.FuelFactory.create_batch(size=5, vehicle=vehicle)
    objs = models.Mileage.objects.get_all_mileage_objects_by_vehicle(vehicle)
    assert objs.count() == 7


@pytest.mark.django_db
def test_get_latest_mileage_by_vehicle():
    mileage = factories.MileageFactory(date='1900-01-01')
    mileage_future = factories.MileageFactory(date='2050-01-01')
    vehicle = factories.VehicleFactory(mileage=mileage)
    service = factories.ServiceFactory(vehicle=vehicle, mileage=mileage_future)
    assert models.Mileage.objects.get_latest_mileage_by_vehicle(
        vehicle
    ) == service.mileage
