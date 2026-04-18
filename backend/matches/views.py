from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Match
from .serializers import MatchSerializer


# CBV APIView — requirement #5b
class MatchListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        matches = Match.objects.all().order_by('date')
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)


# CBV APIView — requirement #5b
class MatchDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            match = Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)
        return Response(MatchSerializer(match).data)