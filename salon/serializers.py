from rest_framework import serializers
from .models import Paket, Booking

class PaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paket
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'