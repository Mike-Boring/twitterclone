from django.shortcuts import render

from tweet.models import Tweet
from twitteruser.models import TwitterUser


def index(request):
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
    all_tweets = Tweet.objects.all().order_by('submission_time').reverse()
    return render(request, "index.html", {"number_tweets": number_tweets, "all_tweets": all_tweets, "profile_user": request.user})


def user_detail_view(request, user_id):
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
    selected_user = TwitterUser.objects.filter(id=user_id).first()
    user_tweets = Tweet.objects.filter(
        twitter_user=user_id).order_by('submission_time').reverse()

    return render(request, "user_profile.html", {"number_tweets": number_tweets, "selected_user": selected_user, "user_tweets": user_tweets, "profile_user": selected_user})
