from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns = [  
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view_gadgets/', views.gadgets, name='gadgets'),
    path('view_gadgets/<int:gadgets_id>', views.edit_gadgets, name='edit_gadgets'),
    path('delete_gadgets/<int:deletegadgets_id>', views.delete_gadgets, name='delete_gadgets'),
    path('view_pastries/', views.pastries, name='pastries'),
    path('view_pastries/<int:pastries_id>', views.edit_pastries, name='edit_pastries'),
    path('delete_pastries/<int:deletepastries_id>', views.delete_pastries, name='delete_pastries'),
    path('view_wears/', views.wears, name='wears'),
    path('upload-gadgets/', views.add_gadgets, name='add_gadgets'),
    path('upload-pastries/', views.add_pastries, name='add_pastries'),
    path('upload-wears/', views.add_wears, name='add_wears'),
    path('view_wears/<int:wears_id>', views.edit_wears, name='edit_wears'),
    path('upload-blog/', views.add_blog, name='add_blog'),
    path('delete-blog/<int:delete_id>', views.delete_blog, name='delete_blog'),
    path('delete-wears/<int:deletewears_id>', views.delete_wears, name='delete_wears'),
    path('list_all_blog/<int:post_id>', views.edit_blog, name='edit_blog'),
    path('view_preview/<int:agent>', views.preview, name='preview'),
    path('subscribers/', views.newsletter, name='newsletter'),
    path('messages/', views.message, name='message'),
    path('reastaurant/', views.food, name='food'),
    path('change-password/', views.change_password, name='change_password'),
    path('view_blog/<int:view_id>', views.view_blog, name='view_blog'),
    path('list_all_blog/', views.list_all_blog, name='list_all_blog'),
     path('change_password/', views.change_password, name='change_password'),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),

]