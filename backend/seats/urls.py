from django.urls import path
from .views import SeatListView, SeatAvailabilityView

urlpatterns = [
    path('',                           SeatListView.as_view()),
    path('availability/<int:match_id>/', SeatAvailabilityView.as_view()),
]