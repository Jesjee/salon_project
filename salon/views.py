from rest_framework import viewsets
from .models import Paket, Booking
from .serializers import PaketSerializer, BookingSerializer

class PaketViewSet(viewsets.ModelViewSet):
    queryset = Paket.objects.all()
    serializer_class = PaketSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer