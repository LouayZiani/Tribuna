from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer
from seats.models import Seat
from matches.models import Match


# CBV APIView — full CRUD on Ticket — requirements #5b + #7 + #8
class TicketListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # READ — list user's own tickets
    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user).select_related('match', 'seat')
        return Response(TicketSerializer(tickets, many=True).data)

    # CREATE — links ticket to request.user — requirement #8
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# CBV APIView — requirement #5b
class TicketDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Ticket.objects.get(pk=pk, user=user)
        except Ticket.DoesNotExist:
            return None

    # READ single
    def get(self, request, pk):
        ticket = self.get_object(pk, request.user)
        if not ticket:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(TicketSerializer(ticket).data)

    # UPDATE (partial) — requirement #7
    def patch(self, request, pk):
        ticket = self.get_object(pk, request.user)
        if not ticket:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    # DELETE — requirement #7
    def delete(self, request, pk):
        ticket = self.get_object(pk, request.user)
        if not ticket:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Free up the seat and increment available count
        seat = ticket.seat
        seat.is_available = True
        seat.save()

        match = ticket.match
        match.available_seats = min(match.total_seats, match.available_seats + 1)
        match.save()

        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)