
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from core.api.viewsets import PontoTuristicoViewSet
from recursos.api.viewsets import RecursoViewSet
from address.api.viewsets import AddressViewSet
from comments.api.viewsets import CommentViewSet
from reviews.api.viewsets import ReviewViewSet


router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'recursos', RecursoViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Linha para conseguir visualisar imagens em modo dev
