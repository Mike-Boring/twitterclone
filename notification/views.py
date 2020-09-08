from django.shortcuts import render

from notification.models import Notification

from twitteruser.models import Relationship

from tweet.models import Tweet


def notification_view(request, user_id):
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user))
    if Relationship.objects.filter(from_person=request.user):
        number_following = len(
            Relationship.objects.filter(from_person=request.user))

    else:
        number_following = 0
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

    return render(
        request, "notifications.html",
        {"user_notifications": user_notifications,
         "notification_tweet": notification_tweet,
         "number_tweets": number_tweets,
         "profile_user": request.user,
         "number_notifications": number_notifications,
         "number_following": number_following,
         "delete_info": delete_info}
    )
