from django.db import models


class Room(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=64
    )
    capacity = models.SmallIntegerField(
        verbose_name='Capacity'
    )
    projector_availability = models.BooleanField(
        verbose_name='Projector availability',
        default=True
    )


class Reservation(models.Model):
    date = models.DateField(
        verbose_name='Date',
    )
    comment = models.CharField(
        verbose_name='Comment',
        max_length=128
    )
    rooms = models.ForeignKey(
        Room,
        verbose_name="Rooms",
        on_delete=models.CASCADE
    )
