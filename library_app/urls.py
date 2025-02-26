from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  LibroViewSet, PrestamoViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]