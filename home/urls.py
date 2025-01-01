from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('',views.home,name='home'),
    path('request_for_suggestionII', views.request_for_suggestionII,name='suggestionII'),
    path('more_land', views.more_land,name='more_land'),
    path('renting_landIV', views.renting_landIV,name='renting_landIV'),
    path('selling_landIII', views.selling_landIII,name='selling_landIII'),
    path('details', views.details,name='details'),
]