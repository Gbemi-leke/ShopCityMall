from django.urls import path
from django.conf.urls import url 
from payments import views

app_name = 'payments'

urlpatterns= [
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('initiate-payment/<str:ref>/', views.verify_payment, name='verify_payment'),

]