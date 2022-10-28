import os
import django
from os import mkdir
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  age = models.IntegerField()

class Song(models.Model):
  Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
  title = models.CharField(max_length = 100)
  date_released = models.DateField()
  likes = models.IntegerField()
  artiste_id = models.CharField(max_length = 30)

class Lyric(models.Model):
  Song = models.ForeignKey(Song, on_delete = models.CASCADE)
  content = models.TextField()
  song_id = models.CharField(max_length = 30)