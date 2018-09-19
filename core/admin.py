from django.contrib import admin


from . import models


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    search_fields = ('name', 'registration',)
    list_display = (
        'name',
        'registration',
        'year_manufactured',
    )


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
