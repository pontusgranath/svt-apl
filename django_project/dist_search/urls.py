from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dist_search-home'),
    path('home/', views.home, name='dist_search-home'),
    path('404/', views.handler404, name='dist_search-404'),
    path('calculate_distance', views.calculate_distance, name='calculate_distance'),
    path('calculate_inline_distance', views.calculate_inline_distance, name='calculate_inline_distance'),
]
