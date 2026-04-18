from django.urls import path
from .views import MatchListView, MatchDetailView

urlpatterns = [
    path('',      MatchListView.as_view()),
    path('<int:pk>/', MatchDetailView.as_view()),
]