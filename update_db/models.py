from django.db import models


class CarMake(models.Model):
    """Марка автомобиля.

    name - название марки.
    updated_at - дата обновления записи.
    """

    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """Модель автомобиля.

    name - название модели.
    updated_at - дата обновления записи.
    """

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
