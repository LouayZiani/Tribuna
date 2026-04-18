from django.db import models
from django.contrib.auth.models import User
from matches.models import Match
from seats.models import Seat


# Model #3 — requirement #1
# ForeignKey Ticket → Match — requirement #3
# ForeignKey Ticket → User  — requirement #3
class Ticket(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    match      = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='tickets')
    seat       = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='tickets')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('match', 'seat')  # one booking per seat per match

    def __str__(self):
        return f'Ticket #{self.id} — {self.user.username} | {self.match}'