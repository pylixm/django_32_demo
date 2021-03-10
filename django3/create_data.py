import string
import datetime
import random
import pytz
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django3.settings'
import django

django.setup()

from blog.models import Blog

starting_at = pytz.UTC.localize(datetime.datetime(2020, 1, 1))
DAY = datetime.timedelta(days=1)

Blog.objects.bulk_create((Blog(
    title=''.join(random.choices(string.ascii_letters + ' ' * 10, k=random.randint(10, 20))),
    create_at=starting_at + (DAY * random.random() * 365),
) for _ in range(10000)))