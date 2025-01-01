from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
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
    price = models.DecimalField(max_digits=10, blank=True, null=True)

    def __str__(self):
        return self.name  # Return the name as the string representation