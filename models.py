from django.db import models
from django.utils import timezone

# Create your models here.
class Initial(models.Model):
    my_truth = models.BooleanField(
        null=True,
        help_text='Please choose True/False',
        verbose_name='Truth',
        )
    my_integer = models.IntegerField(
        null=True, 
        blank=True, 
        default=None,
        help_text='Please set an Integer',
        verbose_name='Integer'
        )
    my_decimal = models.DecimalField(
        null=True, 
        max_digits=48, 
        decimal_places=3, 
        blank=True, 
        default=None,
        help_text='Please give a decimal Value',
        verbose_name='Decimal',)
    my_char = models.CharField(
        max_length=100,
        help_text='Please give it a Name',
        verbose_name='Char',)

    class Meta:
        ordering = ('my_char', 'my_truth', 'my_decimal', 'my_integer')

    def __str__(self):
        return self.my_char


class Subsequent(models.Model):
    your_creation = models.DateTimeField(
        default=timezone.now,
        help_text='Date and Time of creation',
        verbose_name='Creation'
        )
    your_update = models.DateTimeField(
        auto_now=True,
        help_text='Date and Time of last update',
        verbose_name='Update',
        )
    your_initial = models.ForeignKey(
        'Initial',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Please select Initial',
        verbose_name='Initial',
        )
    your_integer = models.IntegerField(
        help_text='Please set an Integer',
        verbose_name='Integer'
        )
    your_char = models.CharField(
        max_length=100,
        help_text='Please give it a Name',
        verbose_name='Char',
        )

    class Meta:
        ordering = ('your_creation', 'your_update', 'your_char', 'your_initial', 'your_integer')

    def __str__(self):
        if self.your_initial:
            return f'{self.your_char} ({self.your_initial} {self.your_creation.year})'
        else: 
            return f'{self.your_char} ({self.your_creation.year})'


class Alternative(models.Model):
    alt_creation = models.DateTimeField(
        default=timezone.now,
        help_text='Date and Time of creation',
        verbose_name='Creation'
        )
    alt_update = models.DateTimeField(
        auto_now=True,
        help_text='Date and Time of last update',
        verbose_name='Update',
        )
    alt_initial = models.ForeignKey(
        'Initial',
        on_delete=models.CASCADE,
        help_text='Please select Initial',
        verbose_name='Initial',
        )
    alt_decimal = models.DecimalField(
        max_digits=48, 
        decimal_places=3, 
        help_text='Please give a decimal Value',
        verbose_name='Decimal',
        )
    alt_char = models.CharField(
        max_length=100,
        help_text='Please give it a Name',
        verbose_name='Alternation',
        )

    class Meta:
        ordering = ('alt_creation', 'alt_update', 'alt_char', 'alt_initial', 'alt_decimal')

    def __str__(self):
        return self.alt_char

class His(Alternative):
    his_integer = models.IntegerField(
        null=True, 
        blank=True, 
        default=None,
        help_text='Please set an Integer',
        verbose_name='Integer'
        )
    his_char = models.CharField(
        max_length=100,
        help_text='Please give it a Name',
        verbose_name='Male',
        )

    class Meta:
        ordering = ('alt_creation', 'alt_update', 'his_char', 'alt_char', 'his_integer', 'alt_decimal')

    def __str__(self):
        return f'{self.alt_char}, {self.his_char}'

class Her(Alternative):
    her_integer = models.IntegerField(
        null=True, 
        blank=True, 
        default=None,
        help_text='Please set an Integer',
        verbose_name='Integer'
        )
    her_char = models.CharField(
        max_length=100,
        help_text='Please give it a Name',
        verbose_name='Female',
        )

    class Meta:
        ordering = ('alt_creation', 'alt_update', 'her_char', 'alt_char', 'her_integer', 'alt_decimal')

    def __str__(self):
        return f'{self.alt_char}, {self.her_char}'