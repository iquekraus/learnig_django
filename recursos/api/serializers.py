from rest_framework import serializers
from recursos.models import Recurso


class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('id', 'name', 'description', 'opening_hours', 'min_age', 'photo')
