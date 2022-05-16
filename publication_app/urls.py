from django.urls import path, include

from publication_app.views import music_page, team_page, main_page, registration_page, login_page, logout_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('team/', team_page, name='team_page'),
    path('radio/', music_page, name='music_page'),
    path('registration/', registration_page, name='reg_page'),
    path('login/', login_page, name='log_page'),
    path('logout/', logout_page, name='logout_page')
]