from django.db import models
from django.utils import timezone
from api.utils import secret_key_gen


class Post(models.Model):
    content = models.CharField(max_length=280)
    category = models.CharField(max_length=1, choices=[
                                ('B', 'Boast'), ('R', 'Roast')])
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    secret_key = models.CharField(max_length=6, default=secret_key_gen)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
