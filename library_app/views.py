from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Libro, Prestamo, Reserva
from .serializers import LibroSerializer, PrestamoSerializer, ReservaSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def reservar(self, request, pk=None):
        libro = self.get_object()
        if not libro.disponible:
            reserva = Reserva.objects.create(
                libro=libro,
                usuario=request.user,
                estado='PENDIENTE'
            )
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "biblioteca_updates",
                {
                    "type": "libro_reservado",
                    "libro_id": libro.id,
                    "usuario": request.user.username
                }
            )
            return Response({'status': 'Libro reservado'})
        return Response({'error': 'Libro no disponible'},
                       status=status.HTTP_400_BAD_REQUEST)

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [IsAuthenticated]

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]