from django.shortcuts import render

from notification.models import Notification


from tweet.models import Tweet


def notification_view(request, user_id):
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user))
    user_notifications = Notification.objects.filter(
        tweeted_user=request.user)
    if len(user_notifications) > 0:
        notification_tweet = user_notifications
    else:
        notification_tweet = ''

    number_notifications = len(notification_tweet)

    def delete_info():
        user_notifications.delete()
        return ''

    # user_notifications.delete()
    return render(request, "notifications.html", {"user_notifications": user_notifications, "notification_tweet": notification_tweet, "number_tweets": number_tweets, "profile_user": request.user, "number_notifications": number_notifications, "delete_info": delete_info})
