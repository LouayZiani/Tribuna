from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Seat
from .serializers import SeatSerializer, SeatAvailabilitySerializer
from matches.models import Match


# CBV APIView — requirement #5b
class SeatListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        match_id = request.query_params.get('match')
        section  = request.query_params.get('section')

        if not match_id:
            return Response({'detail': 'match query param required.'}, status=400)

        qs = Seat.objects.for_match(match_id)
        if section:
            qs = qs.filter(section=section)

        return Response(SeatSerializer(qs, many=True).data)


# CBV APIView — requirement #5b
class SeatAvailabilityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, match_id):
        try:
            match = Match.objects.get(pk=match_id)
        except Match.DoesNotExist:
            return Response({'detail': 'Match not found.'}, status=404)

        seats = Seat.objects.for_match(match_id)
        data = {
            'match_id':          match.id,
            'total_seats':       match.total_seats,
            'available_seats':   match.available_seats,
            'vip_available':     seats.available().filter(section='VIP').count(),
            'regular_available': seats.available().filter(section='Regular').count(),
        }
        serializer = SeatAvailabilitySerializer(data)
        return Response(serializer.data)