from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Alert(models.Model):

    class CustomObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='active')

    options = (
        ('active', 'Active'),
        ('Waiting', 'Waiting'),
        ('Passed', 'Passed'),
    )

    title = models.CharField(max_length=250)
    symbol = models.CharField(max_length=10)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='active')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='api_alarms')
    high_price = models.PositiveIntegerField()
    low_price = models.PositiveIntegerField()

    objects = models.Manager()
    customobjects = CustomObjects()


    def _str__(self):
        return self.title
