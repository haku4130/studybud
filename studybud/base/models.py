from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Category(models.Model):
    pass


class Room(models.Model):
    host = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
