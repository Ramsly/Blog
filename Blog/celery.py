import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')

app = Celery('Blog')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email-newsletter': {
        'task': 'email_newsletter.tasks.send_email_newsletter',
        'schedule': crontab(minute='*/1'),
    }
}
