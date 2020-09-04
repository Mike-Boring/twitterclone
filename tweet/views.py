from django.shortcuts import render, HttpResponseRedirect, reverse

from tweet.forms import TweetForm

from tweet.models import Tweet

from notification.models import Notification

from twitteruser.models import TwitterUser

# Create your views here.


def add_tweet_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            new_tweet = Tweet.objects.create(
                body=data.get('body'),
                twitter_user=request.user
            )
            if '@' in new_tweet.body:
                notification_user = TwitterUser.objects.filter(
                    username='michaelboring').first()
                new_notification = Notification.objects.create(
                    tweeted_user=notification_user,
                    notification_tweets_id=new_tweet.id
                )
            # breakpoint()
            return HttpResponseRedirect(reverse("tweetview", args=[new_tweet.id]))

    form = TweetForm()
    return render(request, "add_tweet.html", {"form": form, "profile_user": request.user})


def tweet_detail_view(request, tweet_id):
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
    my_tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, "tweet_detail.html", {"tweet": my_tweet, "number_tweets": number_tweets, "profile_user": request.user})
