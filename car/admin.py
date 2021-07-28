from django import forms
from django.contrib import admin
from .models import Fuel_Type, Fuel, Manufacturer, Vehicle, Event, Bill, Supplier, Bill_Item_Fuel, Bill_Item_Other
# from .forms import BillItemBaseForm, BillItemOtherForm, BillItemFuelForm

admin.site.site_header = "Administration"

# Register your models here.
class FuelInline(admin.TabularInline):
    model = Fuel
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('name',),
            # 'classes': ('extrapretty',),
        }),
    )
    extra = 0

@admin.register(Fuel_Type)
class FuelTypeSite(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_per_page = 25
    inlines = [
        FuelInline,
    ]
    fieldsets = (
        (None, {
            'fields': ('name', 'description'),
        },
    ),)

@admin.register(Fuel)
class FuelSite(admin.ModelAdmin):
    list_display = ('name', 'fuel_type', )
    search_fields = ('name', 'fuel_type', 'description')
    list_filter = ('fuel_type',)
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (('name', 'fuel_type'), 'description'),
        },
    ),)

class VehicleInline(admin.TabularInline):
    model = Vehicle
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('name', 'licence_plate', 'seats'),
            # 'classes': ('extrapretty',),
        }),
    )
    extra = 0
@admin.register(Manufacturer)
class ManufacturerSite(admin.ModelAdmin):
    list_display = ('name', 'abbr', )
    search_fields = ('name', 'abbr', 'description')
    list_per_page = 25
    inlines = [
        VehicleInline,
    ]
    fieldsets = (
        (None, {
            'fields': (('name', 'abbr'), 'description'),
        },
    ),)

@admin.register(Vehicle)
class VehicleSite(admin.ModelAdmin):
    list_display = ('__str__', 'seats', )
    search_fields = ('name', 'licence_plate', 'manufacturer', 'seats', 'description')
    list_per_page = 25
    # inlines = [
    #     VehicleInline,
    # ]
    fieldsets = (
        (None, {
            'fields': (('name', 'manufacturer'), ('licence_plate', 'seats'), 'description'),
        },
    ),)

@admin.register(Event)
class EventSite(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (('name', 'vehicle'), ('date', 'time'), ('milage', 'trip'), 'description'),
        },
    ),)
class BillItemFuelInline(admin.TabularInline):
    model = Bill_Item_Fuel
    # form = BillItemFuelForm
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('fuel', 'price', 'units', 'total_price', 'tax_included', 'tax_percent'),
            # 'classes': ('extrapretty',),
        }),
    )
    extra = 0

class BillItemOtherInline(admin.TabularInline):
    model = Bill_Item_Other
    # form = BillItemOtherForm
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'price', 'units', 'total_price', 'tax_included', 'tax_percent'),
            # 'classes': ('extrapretty',),
        }),
    )
    extra = 0

@admin.register(Bill)
class BillSite(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_per_page = 25
    inlines = [
        BillItemFuelInline, BillItemOtherInline,
    ]
    fieldsets = (
        (None, {
            'fields': (('name', 'vehicle'), ('date', 'time'), ('milage', 'trip'), 'description'),
        },
    ),)
@admin.register(Supplier)
class SupplierSite(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('name', 'description'),
        },
    ),)

@admin.register(Bill_Item_Fuel)
class BillItemFuelSite(admin.ModelAdmin):
    search_fields = ('name', 'type', 'fuel', 'description')
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (('name', 'type', 'fuel'), ('price', 'units', 'total_price'), ('tax_included', 'tax_percent'), 'description'),
        },
    ),)

@admin.register(Bill_Item_Other)
class BillItemOtherSite(admin.ModelAdmin):
    search_fields = ('name', 'type', 'description')
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (('name', 'type'), ('price', 'units', 'total_price'), ('tax_included', 'tax_percent'), 'description'),
        },
    ),)
