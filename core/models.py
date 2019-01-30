from django.db import models
from recursos.models import Recurso
from comments.models import Comment
from reviews.models import Review
from address.models import Address


class PontoTuristico(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    resources = models.ManyToManyField(Recurso)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

