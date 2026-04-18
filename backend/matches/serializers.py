from rest_framework import serializers
from .models import Match

# ModelSerializer — requirement #4b
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Match
        fields = '__all__'