from django.db import models
# from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from datetime import date

SERVICE = 'SER'
PRODUCT = 'PRD'
ADMIN = 'ADM'
FUEL = 'OEL'
OTHER = 'OTH'
BILL_ITEM_TYPE = [
    (SERVICE, 'Service'),
    (PRODUCT, 'Product'),
    (ADMIN, (
        ('tax', 'Tax'),
        ('prm', 'Permit'),
        ('pnl', 'Penalty'),
    )),
    (FUEL, 'Fuel'),
    (OTHER, 'Other'),
]

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
    abbr = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Short Name of the Name',
        verbose_name='Short Name',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        if self.abbr:
            return self.abbr
        else:
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
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('name',)
        unique_together = ('name', 'licence_plate','manufacturer')

    def __str__(self):
        manufacturer, licence_plate = '', ''
        if self.manufacturer:
            manufacturer = str(self.manufacturer)
        if self.licence_plate:
            licence_plate = f'({self.licence_plate})'
        return ' '.join([
            manufacturer,
            self.name, 
            licence_plate
        ])

class Event(models.Model):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        help_text='Give a name, if applicable',
    )
    vehicle = models.ForeignKey(
        Vehicle, 
        on_delete=CASCADE,
        help_text='Name of Vehicle'
    )
    date = models.DateField(
        auto_now=False, 
        auto_now_add=False, 
        default=date.today,
        help_text='Date of Event',
    )
    time = models.TimeField(
        null=True,
        blank=True,
        default=None,
        help_text='Time of Event',
    )
    milage = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=3,
        max_digits=12,
        help_text='Milage of Car',
    )
    trip = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=3,
        max_digits=12,
        help_text='Trip Distance',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('date', 'vehicle', 'name',)
        unique_together = ('name', 'vehicle', 'date')

    def __str__(self):
        name, time = '', ''
        if self.name:
            name = self.name
        if self.time:
            time = f'{self.time.strftime("%H%M")}'
        return ' '.join([
            f'{str(self.vehicle)} : {self.date.strftime("%Y%m%d")}',
            time,
            name
        ])

class Supplier(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Name of Supplier',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Bill(Event):
    supplier = models.ForeignKey(
        Supplier, 
        null=True,
        blank=True,
        on_delete=SET_NULL,
        help_text='Name of Supplier'
    )

    def __str__(self):
        return f'{self.date.strftime("%Y%m%d")} #{self.id}'
class Bill_Item_Base(models.Model):

    name = models.CharField(
        max_length=100,
        help_text='Type of Bill Item',
    )
    bill = models.ForeignKey(
        Bill, 
        on_delete=CASCADE,
    )
    type = models.CharField(
        max_length=3,
        choices=BILL_ITEM_TYPE,
        default=OTHER,
        help_text='Set Bill Item Type'
    )
    price = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=3,
        max_digits=12,
        help_text='Price per Unit',
    )
    units = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=3,
        max_digits=12,
        help_text='Units purchased',
    )
    total_price = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=3,
        max_digits=12,
        help_text='Total Price paid',
        verbose_name='Total Prize',
    )
    tax_included = models.BooleanField(
        default = True,
        help_text='Are taxes included in unit price and total price? (Brutto = Yes, Netto = No)',
        verbose_name='Tax included?',
    )
    tax_percent = models.DecimalField(
        null=True,
        blank=True,
        default = 19.0,
        decimal_places=3,
        max_digits=12,
        help_text='Percentage of Netto-Price',
        verbose_name='Tax (%)',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     price = cleaned_data.get("price")
    #     units = cleaned_data.get("units")
    #     total_price = cleaned_data.get("total_price")
    #     margin = .001
    #     if price and units and total_price:
    #         from django.core.exceptions import ValidationError
    #         if total_price / units not in range(price - margin, price + margin):
    #             raise ValidationError(f'prices don\'t match: {total_price} / {units} units != {price} ({(total_price / units) - price})')
        
    class Meta:
        ordering = ('name','id')
        verbose_name = 'Bill Item'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'{self.type}: #{self.id}'

class Bill_Item_Fuel(Bill_Item_Base):
    BILL_ITEM_TYPE = [
        (FUEL, 'Fuel'),
        (OTHER, 'Other'),
    ]
    fuel = models.ForeignKey(
        Fuel, 
        on_delete=CASCADE,
        help_text='Name of Fuel'
    )
    class Meta:
        ordering = ('name',)
        verbose_name = 'Bill Item (Fuel)'
        verbose_name_plural = 'Bill Items (Fuel)'

    def __str__(self):
        return self.name

class Bill_Item_Other(Bill_Item_Base):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Bill Item (Other)'
        verbose_name_plural = 'Bill Items (Other)'
