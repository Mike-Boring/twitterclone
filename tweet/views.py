from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic.base import View
from tweet.forms import TweetForm

from tweet.models import Tweet

from notification.models import Notification

from twitteruser.models import TwitterUser, Relationship


# Create your views here.


class AddTweetView(View):
    number_notifications = 0
    number_tweets = 0
    number_following = 0

    def get(self, request):

        if Relationship.objects.filter(from_person=request.user):
            number_following = len(Relationship.objects.filter(
                from_person=request.user))
        else:
            number_following = 0

        user_notifications = Notification.objects.filter(
            tweeted_user=request.user)
        if len(user_notifications) > 0:
            notification_tweet = user_notifications
        else:
            notification_tweet = ''
        number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
        number_notifications = len(notification_tweet)
        form = TweetForm()
        return render(
            request, "add_tweet.html",
            {"form": form,
             "profile_user": request.user,
             "number_notifications": number_notifications,
             "number_tweets": number_tweets,
             "number_following": number_following}
        )

    def post(self, request):
        user_notifications = Notification.objects.filter(
            tweeted_user=request.user)
        number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
        if len(user_notifications) > 0:
            notification_tweet = user_notifications
        else:
            notification_tweet = ''
        number_notifications = len(notification_tweet)
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                body=data.get('body'),
                twitter_user=request.user
            )
            if '@' in new_tweet.body:
                split_body = new_tweet.body.split()
                extracted_username = ''
                for word in split_body:
                    if word.startswith('@'):
                        extracted_username = word.replace('@', '')
                notification_user = TwitterUser.objects.filter(
                    username=extracted_username).first()
                Notification.objects.create(
                    tweeted_user=notification_user,
                    notification_tweets_id=new_tweet.id
                )
            return HttpResponseRedirect(
                reverse("tweetview", args=[new_tweet.id])
            )
        return render(
            request, "add_tweet.html",
            {"form": form,
             "profile_user": request.user,
             "number_notifications": number_notifications,
             "number_tweets": number_tweets}
        )


def tweet_detail_view(request, tweet_id):
    number_notifications = 0
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(
            tweeted_user=request.user)
        if len(user_notifications) > 0:
            notification_tweet = user_notifications
        else:
            notification_tweet = ''
        number_notifications = len(notification_tweet)
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
    my_tweet = Tweet.objects.filter(id=tweet_id).first()
    if Relationship.objects.filter(from_person=request.user):
        number_following = len(Relationship.objects.filter(
            from_person=request.user))
    else:
        number_following = 0
    return render(
        request, "tweet_detail.html",
        {"tweet": my_tweet,
         "number_tweets": number_tweets,
         "profile_user": request.user,
         "number_notifications": number_notifications,
         "number_following": number_following}
    )
