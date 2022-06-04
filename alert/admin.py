from django.contrib import admin
from . import models


@admin.register(models.Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'author', 'symbol',
                    'high_price', 'low_price')
