from django import forms
from django.contrib import admin
from .models import Fuel_Type, Fuel, Manufacturer, Vehicle

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
    search_fields = ('name', 'fuel_type', 'description')
    list_filter = ('fuel_type',)
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (('name', 'fuel_type'), 'description'),
        },
    ),)