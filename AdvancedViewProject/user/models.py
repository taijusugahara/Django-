from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
# Create your models here.

class Profile(models.Model):
  user = OneToOneField(User, on_delete=models.CASCADE)
  website = models.URLField(blank=True)
  picture = models.FileField(upload_to='user/', blank=True)

  def __str__(self):
    return self.user.username