# Generated by Django 3.1.1 on 2020-09-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_tweet_twitter_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=140),
        ),
    ]
