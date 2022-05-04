from django.urls import path

from publication_app.views import music_page, team_page, main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('team/', team_page, name='team_page'),
    path('radio/', music_page, name='music_page')
]