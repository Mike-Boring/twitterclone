from django.shortcuts import render

from notification.models import Notification


from tweet.models import Tweet


def notification_view(request, user_id):
    user_notifications = Notification.objects.filter(
        tweeted_user=request.user)
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user))
    if len(user_notifications) > 0:
        notification_tweet = user_notifications
    else:
        notification_tweet = 'No Notifications Found'

    return render(request, "notifications.html", {"user_notifications": user_notifications, "notification_tweet": notification_tweet, "number_tweets": number_tweets, "profile_user": request.user})
