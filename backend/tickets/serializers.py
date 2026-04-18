from rest_framework import serializers
from .models import Ticket
from matches.serializers import MatchSerializer
from seats.serializers import SeatSerializer


# ModelSerializer — requirement #4b
class TicketSerializer(serializers.ModelSerializer):
    match_details = MatchSerializer(source='match', read_only=True)
    seat_details  = SeatSerializer(source='seat',  read_only=True)

    class Meta:
        model  = Ticket
        fields = ['id', 'match', 'seat', 'user', 'created_at', 'match_details', 'seat_details']
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        seat  = data.get('seat')
        match = data.get('match')

        if seat.match_id != match.id:
            raise serializers.ValidationError('This seat does not belong to the selected match.')
        if not seat.is_available:
            raise serializers.ValidationError('This seat is already taken.')
        return data

    def create(self, validated_data):
        seat = validated_data['seat']

        # Mark seat as unavailable
        seat.is_available = False
        seat.save()

        # Decrement available_seats on Match
        match = validated_data['match']
        match.available_seats = max(0, match.available_seats - 1)
        match.save()

        return super().create(validated_data)