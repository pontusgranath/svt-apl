from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='dist_search-home'),
    url(r'^calculate_distance', views.calculate_distance),
]
