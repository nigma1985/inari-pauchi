from django.contrib import admin
from .models import Manufacturer, Series, Vehicle

# Register your models here.
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    # name, abbr, logo, note
    search_fields = ('name', 'abbr', 'note', )
    list_per_page = 100
    fieldsets = (
        (None, {
            'fields': (('name', 'abbr'), 'logo', 'note', ),
        },
    ),)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    # name, abbr, manufacturer, note
    search_fields = ('name', 'abbr', 'note', )
    list_per_page = 100
    fieldsets = (
        (None, {
            'fields': (('name', 'abbr'), 'manufacturer', 'note', ),
        },
    ),)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # series, version, nickname, licence_plate, seats, description
    search_fields = ('version', 'nickname', 'licence_plate', 'seats', 'description')
    list_per_page = 100
    fieldsets = (
        (None, {
            'fields': (('series', 'version'), 'nickname', ('licence_plate', 'seats'), 'image', 'description', ),
        },
    ),)
