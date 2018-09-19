from django.conf.urls import url
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.views.generic import TemplateView

from core.utils import get_vehicle_costs
from . import models


class VehicleTotalCostView(TemplateView):
    template_name = 'core/vehicle-total-cost.html'

    def get_context_data(self, **kwargs):
        costs = get_vehicle_costs(vehicle_pk=self.kwargs['pk'])
        return super(VehicleTotalCostView, self).get_context_data(
            data=costs,
            opts=models.Vehicle._meta,
            has_view_permission=True,
            original='Vehicle total cost',
            **kwargs
        )


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    search_fields = ('name', 'registration',)
    list_display = (
        'name',
        'registration',
        'year_manufactured',
        'total_cost'
    )

    def total_cost(self, obj):
        return format_html('<a href="{url}">View total costs</a>'.format(
            url=reverse("admin:vehicle-total-cost", kwargs={'pk': obj.pk})
        ))

    def get_urls(self):
        return [
                   url(
                       r'^(?P<pk>[0-9]+)/total-costs/$',
                       self.admin_site.admin_view(
                           VehicleTotalCostView.as_view()
                       ),
                       name="vehicle-total-cost"
                   ),
               ] + super(VehicleAdmin, self).get_urls()

    total_cost.short_description = 'Total costs'
    total_cost.allow_tags = True


@admin.register(models.Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date',)
    list_filter = ('vehicle', )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'vehicle',
        'type_of_service',
        'miles',
        'cost'
    )
    list_filter = (
        'vehicle',
        'type_of_service',
    )


@admin.register(models.Mileage)
class MileageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date', 'miles')
    list_filter = ('vehicle', )


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date', 'description', 'cost')
    list_filter = ('vehicle', )
