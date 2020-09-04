from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your models here.

# received some guidance from Peter Marsh on FK for notification_tweets_id


class Notification(models.Model):
    tweeted_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    notification_tweets = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.notification_tweets.body
