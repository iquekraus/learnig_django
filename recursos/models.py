from django.db import models


class Recurso(models.Model):

    name = models.CharField(max_length=150, default='')
    description = models.TextField(default='')
    opening_hours = models.CharField(max_length=150, default='')
    min_age = models.IntegerField(default=18)
    photo = models.ImageField(upload_to='recursos', null=True, blank=True)

    def __str__(self):
        return self.name
