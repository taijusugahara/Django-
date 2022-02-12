import uuid
from django.db import models
from django.utils import timezone


class Message(models.Model):
    content = models.TextField()