from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    ingredient = models.ManyToManyField(Ingredient)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
