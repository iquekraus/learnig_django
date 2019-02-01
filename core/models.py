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
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)


    @property
    def is_approved(self):
        if self.approved:
            return 'Yes, it is approved!'
        return 'Oh no, very embarrassing!'


    def __str__(self):
        return self.name

