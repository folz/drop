from django.db import models

from django.contrib.gis.db import models as geo_models


class Note(models.Model):
    user_id = models.CharField(max_length=255)
    point = geo_models.PointField()

    class Meta:
        abstract = True

class TextNote(Note):
    text = models.TextField()

class ImageNote(Note):
    objects = geo_models.GeoManager()
    image = models.TextField()
    actual_image = models.ImageField(upload_to="images", null=True, blank=True)
    
    def get_absolute_url(self):
        return "/#{}".format(self.pk)

class VideoNote(Note):
    video = models.FileField(upload_to="videos")
