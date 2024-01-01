from django.urls import path
from django.conf.urls import url 
from users import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

]