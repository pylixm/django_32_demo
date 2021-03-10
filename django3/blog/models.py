from django.db import models
from django.db.models import F, Value
from django.db.models.functions import Lower, Upper


class Blog(models.Model):
    title = models.CharField(max_length=1000)
    create_at = models.DateTimeField()

