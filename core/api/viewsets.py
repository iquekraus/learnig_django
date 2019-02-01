from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'address__zip_code')

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


    def get_queryset(self):

        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        approved = self.request.query_params.get('approved', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)

        if name:
            queryset = queryset.filter(name=name)

        if approved:
            queryset = queryset.filter(approved=approved)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
        ## return Response({'teste': 123})

    def create(self, request, *args, **kwargs):
       return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
       return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs): ## GET by ID
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
       return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
       return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # Actions personalisados:
    # @action(methods=['get'], detail=True) ## Datail=True quando for by ID
    # def denunciar(self, request, pk=None):
    #     pass
    #
    # @action(methods=['get'], detail=False) ## Datail=False quando não for by ID
    # def teste(self, request):
    #     pass
