from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from twitteruser.models import Relationship


@login_required
def index(request):
    number_tweets = len(Tweet.objects.filter(twitter_user=request.user.id))
    user_tweets = Tweet.objects.filter(
        twitter_user=request.user.id).order_by('submission_time').reverse()

    if Relationship.objects.filter(from_person=request.user):
        relationship_list = Relationship.objects.filter(
            from_person=request.user)

        all_follow_tweets = []
        for relationship in relationship_list:
            all_follow_tweets.append(Tweet.objects.filter(
                twitter_user=relationship.to_person))
        follow_tweets = all_follow_tweets
        number_following = len(Relationship.objects.filter(
            from_person=request.user))
    else:
        follow_tweets = ""
        number_following = 0

    number_notifications = 0
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(
            tweeted_user=request.user)
        if len(user_notifications) > 0:
            notification_tweet = user_notifications
        else:
            notification_tweet = ''

        number_notifications = len(notification_tweet)

    return render(
        request, "index.html",
        {"number_tweets": number_tweets,
         "all_tweets": user_tweets,
         "follow_tweets": follow_tweets,
         "profile_user": request.user,
         "number_notifications": number_notifications,
         "number_following": number_following}
    )


def user_detail_view(request, user_id):
    number_notifications = 0
    if request.user.is_authenticated:
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

    if Relationship.objects.filter(
            to_person=user_id, from_person=request.user):
        relationship_status = True
    else:
        relationship_status = False

    return render(
        request, "user_profile.html",
        {"number_tweets": number_tweets,
         "selected_user": selected_user,
         "user_tweets": user_tweets,
         "profile_user": selected_user,
         "number_notifications": number_notifications,
         "relationship_status": relationship_status}
    )


def add_relationship(request, to_person):
    person_user = TwitterUser.objects.filter(username=to_person).first()
    Relationship.objects.create(
        from_person=request.user,
        to_person=person_user
    )
    return HttpResponseRedirect(reverse("userview", args=[person_user.id]))
    # return render(request, "/user/{person_user.id}/")


def remove_relationship(request, to_person):
    person_user = TwitterUser.objects.filter(username=to_person).first()
    relationship_to_delete = Relationship.objects.filter(
        from_person=request.user,
        to_person=person_user
    )
    relationship_to_delete.delete()

    return HttpResponseRedirect(reverse("userview", args=[person_user.id]))
