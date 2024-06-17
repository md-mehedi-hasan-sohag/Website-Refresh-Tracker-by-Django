from django.db import models
from django.utils import timezone

class RefreshCounter(models.Model):
    total_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Refresh Count: {self.count}"
    
class DailyRefreshCounter(models.Model):
    date = models.DateField(default=timezone.now)
    daily_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} - Daily Refresh Count: {self.daily_count}"
