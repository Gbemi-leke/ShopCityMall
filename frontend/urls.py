from django.urls import path
from django.conf.urls import url 
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('restaurant/', views.foods, name='foods'),
    path('wears/', views.wears, name='wears'),
    path('make-payment/', views.payment, name='payment'),
    path('wears_detail/<int:wears_id>/', views.wears_details, name='wears_details'),
    path('phones/', views.phones, name='phones'),
    path('cakes/', views.cakes, name='cakes'),
    path('pastries_detail/<int:cake_id>/', views.cake_details, name='cake_details'),
    path('gadgets_detail/<int:phones_id>/', views.phone_details, name='phone_details'),
    path('blog/', views.blog, name='blog'),
    path('hostel/', views.hostel, name='hostel'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:detail_id>/', views.blog_details, name='blog_details'), 

]