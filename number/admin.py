from django.contrib import admin
from .models import RefreshCounter, DailyRefreshCounter

# Register your models here.
admin.site.register(RefreshCounter)
admin.site.register(DailyRefreshCounter)