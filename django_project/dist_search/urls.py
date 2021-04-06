from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dist_search-home'),
    path('home/', views.home, name='dist_search-home'),
    path('calculate_distance', views.calculate_distance, name='calculate_distance'),
]
