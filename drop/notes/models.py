from django.db import models

from django.contrib.gis.db import models as geo_models


class Note(models.Model):
    point = geo_models.PointField()
