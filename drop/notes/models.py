from django.db import models

from django.contrib.gis.db import models as geo_models


class Note(models.Model):
    point = geo_models.PointField()

    class Meta:
        abstract = True

class TextNote(Note):
    text = models.TextField()

class ImageNote(Note):
    image = models.ImageField(upload_to="images")

class VideoNote(Note):
    video = models.FileField(upload_to="videos")