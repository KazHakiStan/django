from django.urls import path
from loginsys_app.views import login_page, logout_page, registration_page

urlpatterns = [
    path('login/', login_page),
    path('logout/', logout_page),
    path('registration/', registration_page),

]