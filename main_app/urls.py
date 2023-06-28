from django.urls import path
from . import views

urlpatterns = [
    # This first path tells me that it's looking in views.py for a class that's named Home at localhost:8000/
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('songs/', views.SongList.as_view(), name="song_list"),
    # This is telling me if I hit the URL artists/new, I should see a class named ArtistCreate in the views
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    path('artists/<int:pk>/update', views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name="artist_delete"),
    path('artists/<int:pk>/songs/new', views.SongCreate.as_view(), name="song_create"),
    path('playlists/<int:pk>/songs/<int:song_pk>/', views.PlaylistSongAssoc.as_view(), name="playlist_song_assoc"),
]