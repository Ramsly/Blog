from django.core.mail import send_mail
from Blog.celery import app

from .models import Newsletter


@app.task
def send_email_newsletter():
    for user in Newsletter.objects.all():
        send_mail(
            'News. Newsletter',
            'Message',
            'theluckyfeed1@gmail.com',
            [user.email],
            fail_silently=False
        )
