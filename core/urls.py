import django
from django.urls import path
from . views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home' ),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', MyloginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]
