from rest_framework.viewsets import ModelViewSet
from recursos.models import Recurso
from recursos.api.serializers import RecursoSerializer


class RecursoViewSet(ModelViewSet):

    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    filter_fields = ('id', 'name', 'description')
