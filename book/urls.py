from django.urls import path
from . import views

app_name='book'

urlpatterns = [
    path('', views.home, name='home'),
    # path('category/<slug:slug>/', views.home, name='category'),
    path('service/<slug:service>/', views.service_detail, name='service'),
    path('booking', views.service_detail, name='booking'),
    path('category/<slug:category>/', views.category, name='category'),
    path('services/', views.category, name='services'),
    path('bookings/', views.all_booking, name='bookings'),
]
