# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(1886)
        ]
    )
    dealer_id = models.IntegerField()
    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ('PETROL', 'Petrol'),
            ('DIESEL', 'Diesel'),
            ('ELECTRIC', 'Electric'),
            ('HYBRID', 'Hybrid'),
        ],
        default='PETROL'
    )
    transmission = models.CharField(
        max_length=20,
        choices=[
            ('MANUAL', 'Manual'),
            ('AUTOMATIC', 'Automatic'),
        ],
        default='MANUAL'
    )
    color = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.type})"
