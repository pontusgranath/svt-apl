from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dist_search-home'),
    path('home/', views.home, name='dist_search-home'),
    path('404/', views.handler404, name='dist_search-404'),
    path('500/', views.handler500, name='dist_search-500'),
    path('calculate_distance', views.calculate_distance, name='calculate_distance'),
    path('calculate_inline_distance', views.calculate_inline_distance, name='calculate_inline_distance'),
]

handler404 = 'dist_search.views.handler404'
handler500 = 'dist_search.views.handler500'