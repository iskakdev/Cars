from django.db import models

class CarMake(models.Model):
    car_make_name = models.CharField(max_length=77, unique=True)

    def __str__(self):
        return f'{self.car_make_name}'


class CarProduct(models.Model):
    car_name = models.CharField(max_length=66)
    price = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    mileages = models.PositiveIntegerField()
    description = models.TextField()
    color = models.CharField(max_length=25)
    created_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.car_name}'
