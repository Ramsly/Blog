from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(max_length=100, default="", unique=True)

    def __str__(self):
        return f'{self.email}'
