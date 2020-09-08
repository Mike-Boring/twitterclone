"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication.views import login_view, logout_view, signup_view
from tweet.views import add_tweet_view, tweet_detail_view
from twitteruser.views import (
    index, user_detail_view, remove_relationship, add_relationship,
    AddRelationship
)

from notification.views import notification_view

urlpatterns = [
    path('', index, name='homeview'),
    path('login/', login_view, name='loginview'),
    path('tweet/<int:tweet_id>/', tweet_detail_view, name="tweetview"),
    path('addtweet/', add_tweet_view, name="addtweetview"),
    path('user/<int:user_id>/', user_detail_view, name="userview"),
    path('user/<int:user_id>/notifications',
         notification_view, name="notificationview"),
    path('user/addfollow/<str:to_person>',
         add_relationship, name="addrelationship"),
    path('user/addfollow/<str:to_person>',
         AddRelationship.as_view()),
    path('user/removefollow/<str:to_person>',
         remove_relationship, name="removerelationship"),
    path('signup/', signup_view, name='signupview'),
    path('logout/', logout_view, name='logoutview'),
    path('admin/', admin.site.urls),
]
