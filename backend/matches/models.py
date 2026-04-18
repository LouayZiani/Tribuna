from django.db import models

# Model #1 — requirement #1
class Match(models.Model):
    home_team      = models.CharField(max_length=100)
    away_team      = models.CharField(max_length=100)
    date           = models.DateTimeField()
    stadium        = models.CharField(max_length=100)
    city           = models.CharField(max_length=100)
    total_seats    = models.PositiveIntegerField(default=200)
    available_seats = models.PositiveIntegerField(default=200)
    vip_price      = models.PositiveIntegerField(default=15000)   # KZT
    regular_price  = models.PositiveIntegerField(default=5000)    # KZT

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} — {self.date:%Y-%m-%d}'