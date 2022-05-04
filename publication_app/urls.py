from django.urls import path

from publication_app.views import main_page, team_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('team/', team_page, name='team_page')
]