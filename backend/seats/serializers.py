from rest_framework import serializers
from .models import Seat

# ModelSerializer — requirement #4b
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Seat
        fields = '__all__'


# serializers.Serializer — requirement #4a
class SeatAvailabilitySerializer(serializers.Serializer):
    match_id        = serializers.IntegerField()
    total_seats     = serializers.IntegerField()
    available_seats = serializers.IntegerField()
    vip_available   = serializers.IntegerField()
    regular_available = serializers.IntegerField()