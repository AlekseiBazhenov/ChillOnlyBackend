from django.db import models


class Station(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    player_url = models.CharField(max_length=1000)
    station_url = models.CharField(max_length=250)
    image = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title
