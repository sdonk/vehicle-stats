from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from moneyed import Money, GBP

from core.models import Vehicle


def get_vehicle_costs(vehicle_pk):
    vehicle = Vehicle.objects.prefetch_related(
        'fuel_set',
        'service_set',
        'purchase_set'
    ).filter(
        pk=vehicle_pk
    ).annotate(
        total_fuel_cost=Coalesce(Sum('fuel__cost'), Value(0)),
        total_services_cost=Coalesce(Sum('service__cost'), Value(0)),
        total_purchases_cost=Coalesce(Sum('purchase__cost'), Value(0))
    )
    return {
        'purchase': vehicle.cost_of_purchase,
        'fuel': Money(vehicle.total_fuel_cost, GBP),
        'services': Money(vehicle.total_services_cost, GBP),
        'purchases': Money(vehicle.total_purchases_cost, GBP),
        'total': Money(
            sum((
                vehicle.cost_of_purchase.amount,
                vehicle.total_fuel_cost,
                vehicle.total_services_cost,
                vehicle.total_purchases_cost
            )),
            GBP)
    }
