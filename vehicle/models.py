from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from PIL import Image

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Name',
        verbose_name='Name',
    )
    abbr = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text='Abbrivation of Name',
        verbose_name='Short Name',
    )
    logo = models.ImageField(
        default='default.jpg', 
        upload_to='manufacturer_logo',
        help_text='upload logo',
        verbose_name='Logo'
    )
    note = models.TextField(
        null=True,
        blank=True,
        help_text='Open space for notes of all sorts',
        verbose_name='Note',
    )
    class Meta:
        ordering = ('name', )

    def __str__(self):
        if self.abbr:
            return self.abbr
        else:
            return self.name

    def save(self):
        super().save()
        img = Image.open(self.logo.path)
        if img.height > 100 or img.width > 100:
            form_factor = max([img.height, img.width]) / min([img.height, img.width])
            size = min([100, img.height, img.width]) * form_factor
            output_size = (size, size)
            img.thumbnail(output_size)
        img.save(self.logo.path)


class Series(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Name',
        verbose_name='Name',
    )
    abbr = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text='Abbrivation of Name',
        verbose_name='Short Name',
    )
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=CASCADE,
        help_text='Select Manufacturer',
    )
    note = models.TextField(
        null=True,
        blank=True,
        help_text='Open space for notes of all sorts',
        verbose_name='Note',
    )
    class Meta:
        ordering = ('manufacturer', 'name', )
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    def __str__(self):
        if self.abbr:
            return f'{str(self.manufacturer)} {self.abbr}'
        else:
            return f'{str(self.manufacturer)} {self.name}'

class Vehicle(models.Model):
    series = models.ForeignKey(
        Series, 
        on_delete=SET_NULL,
        null=True,
        blank=True,
        help_text='Name of Manufacturer\'s Series',
    )
    version = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Version of Series (i.e. Number)',
        verbose_name='Version',
    )
    nickname = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Nickname of vehicle',
        verbose_name='Nickname',
    )
    licence_plate = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Current Licence Plate of Vehicle',
    )
    seats = models.SmallIntegerField(
        default=5,
        help_text='maximum number of passangers',
    )
    image = models.ImageField(
        default='default.jpg', 
        upload_to='vehicle_image',
        help_text='upload logo',
        verbose_name='Logo'
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('series', 'version', 'licence_plate')
        unique_together = ('series', 'version', 'licence_plate')

    def __str__(self):
        license_plate = ''
        if self.licence_plate:
            license_plate = f' ({self.licence_plate})'
        if self.nickname:
            return f'{self.nickname}{license_plate}'
        return  f'{self.series} {self.version}{license_plate}'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            form_factor = max([img.height, img.width]) / min([img.height, img.width])
            size = min([300, img.height, img.width]) * form_factor
            output_size = (size, size)
            img.thumbnail(output_size)
        img.save(self.image.path)