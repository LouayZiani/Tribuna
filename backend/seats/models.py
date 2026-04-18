from django.db import models
from matches.models import Match


class AvailableSeatManager(models.Manager):
    """Custom manager — requirement #2"""
    def available(self):
        return self.filter(is_available=True)

    def for_match(self, match_id):
        return self.filter(match_id=match_id)


# Model #2 — requirement #1
# ForeignKey Seat → Match — requirement #3
class Seat(models.Model):
    SECTION_CHOICES = [('VIP', 'VIP'), ('Regular', 'Regular')]

    match        = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='seats')
    row          = models.CharField(max_length=2)
    number       = models.PositiveIntegerField()
    section      = models.CharField(max_length=10, choices=SECTION_CHOICES)
    is_available = models.BooleanField(default=True)

    objects = AvailableSeatManager()  # custom manager

    class Meta:
        unique_together = ('match', 'row', 'number')

    def __str__(self):
        return f'{self.section} Row {self.row} Seat {self.number} (Match {self.match_id})'