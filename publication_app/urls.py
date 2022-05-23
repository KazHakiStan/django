from django.urls import path

from publication_app.views import music_page, team_page, main_page, posts_page, profile_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('team/', team_page, name='team_page'),
    path('radio/', music_page, name='music_page'),
    path('posts/all', posts_page, name='posts_page'),
    path('profile/', profile_page)
    # path(r'^posts/get/(?P<publication_app_post_id>\d+)/$', post_page, name='post_page'),
]