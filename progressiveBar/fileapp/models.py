from django.db import models

class File(models.Model):
  title = models.CharField(max_length=250)
  file = models.FileField(upload_to='file')


