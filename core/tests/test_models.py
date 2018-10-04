from decimal import Decimal

import pytest

from . import factories


@pytest.mark.django_db
def test_calculate_price_per_litre():
    fuel = factories.FuelFactory(
        cost=41.50,
        litres=32.26
    )

    assert fuel.price_per_litre.amount == Decimal('1.286')


@pytest.mark.django_db
def test_calculate_litres():
    fuel = factories.FuelFactory(
        cost=41.50,
        price_per_litre=1.286
    )

    assert fuel.litres == Decimal('32.27')


@pytest.mark.django_db
def test_litres_and_price_per_litre_defined_by_user():
    fuel = factories.FuelFactory(
        cost=41.50,
        price_per_litre=1,
        litres=1
    )

    assert fuel.price_per_litre.amount == Decimal('1')
    assert fuel.litres == Decimal('1')


@pytest.mark.django_db
def test_litres_and_price_per_litre_cannot_be_calculated():
    fuel = factories.FuelFactory(
        cost=41.50,
    )

    assert fuel.price_per_litre is None
    assert fuel.litres is None
