from django.db import models


class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.street
