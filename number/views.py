from django.shortcuts import render
from django.utils import timezone
from .models import RefreshCounter, DailyRefreshCounter
from datetime import timedelta

def refresh_view(request):
    # Update total refresh count
    total_counter, created = RefreshCounter.objects.get_or_create(id=1)
    total_counter.total_count += 1
    total_counter.save()

    # Update daily refresh count
    today = timezone.now().date()
    daily_counter, created = DailyRefreshCounter.objects.get_or_create(date=today)
    daily_counter.daily_count += 1
    daily_counter.save()

    # Get yesterday's date and refresh count
    yesterday = today - timedelta(days=1)
    try:
        yesterday_counter = DailyRefreshCounter.objects.get(date=yesterday)
        yesterday_count = yesterday_counter.daily_count
    except DailyRefreshCounter.DoesNotExist:
        yesterday_count = 0
        
    context = {
        'total_count': total_counter.total_count,
        'daily_count': daily_counter.daily_count,
        'yesterday_count': yesterday_count,
        'date': today,
        'yesterday': yesterday
    }
    return render(request, 'counter/refresh.html', context)
