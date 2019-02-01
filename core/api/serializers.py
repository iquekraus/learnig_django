from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.models import PontoTuristico
from recursos.api.serializers import RecursoSerializer
from address.api.serializers import AddressSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):

    resources = RecursoSerializer(many=True)
    address = AddressSerializer()
    comments = CommentSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    name_with_description = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'name', 'description', 'name_with_description',
                  'is_approved', 'approved', 'photo', 'address', 'resourses', 'comments', 'reviews')

    def get_name_with_description(self, obj): # É melhor fazer isso nos models, parecido com a funcao is_approved
        return '%s - %s' % (obj.name, obj.description)
