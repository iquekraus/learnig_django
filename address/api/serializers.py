from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'zip_code', 'street', 'city', 'state', 'district', 'number')
