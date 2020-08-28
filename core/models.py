import uuid
import datetime

from django.db import models
from django.utils import timezone


class Gallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return str(self.id)


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    upload = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return str(self.id)
