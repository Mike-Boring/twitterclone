from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class TwitterUser(AbstractUser):
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')


class Relationship(models.Model):
    from_person = models.ForeignKey(
        TwitterUser, related_name='from_people', on_delete=models.CASCADE)
    to_person = models.ForeignKey(
        TwitterUser, related_name='to_people', on_delete=models.CASCADE)
    relationship_status = models.BooleanField(default=True)
