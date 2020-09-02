from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

# Create your models here.


class Tweet(models.Model):
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=240)
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
