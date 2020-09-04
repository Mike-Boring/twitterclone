from django.shortcuts import render

from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification


def index(request):
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
    all_tweets = Tweet.objects.all().order_by('submission_time').reverse()
    number_notifications = 0
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(
            tweeted_user=request.user)
        if len(user_notifications) > 0:
            notification_tweet = user_notifications
        else:
            notification_tweet = ''

        number_notifications = len(notification_tweet)

    return render(request, "index.html", {"number_tweets": number_tweets, "all_tweets": all_tweets, "profile_user": request.user, "number_notifications": number_notifications})


def user_detail_view(request, user_id):
    user_notifications = Notification.objects.filter(
        tweeted_user=request.user)
    if len(user_notifications) > 0:
        notification_tweet = user_notifications
    else:
        notification_tweet = ''

    number_notifications = len(notification_tweet)

    number_tweets = len(Tweet.objects.filter(twitter_user=user_id))
    selected_user = TwitterUser.objects.filter(id=user_id).first()
    user_tweets = Tweet.objects.filter(
        twitter_user=user_id).order_by('submission_time').reverse()

    return render(request, "user_profile.html", {"number_tweets": number_tweets, "selected_user": selected_user, "user_tweets": user_tweets, "profile_user": selected_user, "number_notifications": number_notifications})
