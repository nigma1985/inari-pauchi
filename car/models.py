from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Fuel_Type(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Fuel Type Name',
        verbose_name='Type',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('name',)
        verbose_name = 'Fuel Type'

    def __str__(self):
        return self.name
class Fuel(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Fuel Name',
        verbose_name='Name',
    )
    fuel_type = models.ForeignKey(
        Fuel_Type, 
        on_delete=CASCADE,
        help_text='Fuel Type',
        verbose_name='Type',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return f'{self.name} ({self.fuel_type})'
class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Fuel Type Name',
        verbose_name='Type',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Name, Model or Nickname of vehicle',
        verbose_name='Name',
    )
    licence_plate = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Current Licence Plate of Vehicle',
    )
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=SET_NULL,
        null=True,
        blank=True,
        help_text='Name of Manufacturer',
    )
    seats = models.SmallIntegerField(
        default=5,
        help_text='maximum number of passangers',
    )
    class Meta:
        ordering = ('name',)
        unique_together = ('name', 'licence_plate',)

    def __str__(self):
        if self.licence_plate:
            return f'{self.name} ({self.licence_plate})'
        return self.name

# class Event(models.Model):
#     pass

# class Bill(models.Model):
#     pass

# class Bill_Item_Types(models.Model):
#     pass

# class Bill_Item_Base(models.Model):
#     pass

# class Bill_Item_Fuel(models.Model):
#     pass

# class Bill_Item_Other(models.Model):
#     pass
