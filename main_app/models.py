from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)
    verified_artist = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "Artist: " + self.name

    # This is a way to make sure that the data is saved in the order of the names. Alphabetically sorted
    class Meta:
        ordering = ['name']

class Song(models.Model):
    title = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title
    
    def get_length(self):
        return time.strftime("%M:%S", time.gmtime(self.length))
    
class Playlist(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
