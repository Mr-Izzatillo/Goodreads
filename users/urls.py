from django.urls import path
from .views import Register, Login, Logaut, Profile, Prifile_edit
app_name = 'users'
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logaut/', Logaut.as_view(), name='logaut'),
    path('profile/', Profile.as_view(), name='profile'),
    path('edit/', Prifile_edit.as_view(), name='profile_edit')
]
