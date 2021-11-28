from django.db import models
from django.urls import reverse_lazy
from django.dispatch import receiver
import os
import logging

application_logger = logging.getLogger('application-logger')


class BaseModel(models.Model):
  created_at = models.DateTimeField()
  update_at = models.DateTimeField()

  class Meta:
    abstract = True


class Books(BaseModel):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
 

  class Meta:
    db_table = 'books'

  def get_absolute_url(self):
      return reverse_lazy('store:detail_book',kwargs={'pk' : self.pk})


class PictureManager(models.Manager):
  def fillter_by_book(self,book):
    return self.filter(book=book).all()


class Pictures(BaseModel):
  picture = models.FileField(upload_to='picture/')
  book = models.ForeignKey(
  'books',on_delete=models.CASCADE
  )
  objects = PictureManager()

  class Meta:
    db_table = 'pictures'

@receiver(models.signals.post_delete, sender=Pictures)
def delete_picture(sender,instance,**kwargs):
  if instance.picture:
    if os.path.isfile(instance.picture.path):
      os.remove(instance.picture.path)
      application_logger.info(f'{instance.picture.path}を削除しました')
    


