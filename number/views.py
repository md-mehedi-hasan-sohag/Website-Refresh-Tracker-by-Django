from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from .models import RefreshCounter, DailyRefreshCounter

def refresh_view(request):
    total_counter, created = RefreshCounter.objects.get_or_create(id=1)
    total_counter.total_count += 1
    total_counter.save()

    today = timezone.now().date()
    daily_counter, created = DailyRefreshCounter.objects.get_or_create(date=today)
    daily_counter.daily_count += 1
    daily_counter.save()

    context = {
        'total_count': total_counter.total_count,
        'daily_count': daily_counter.daily_count,
        'date': today
    }
    return render(request, 'counter/refresh.html', context)
