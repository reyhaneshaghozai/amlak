from django.urls import path
from. import views


urlpatterns = [
    path('',views.home,name='home'),
    path('sell/',views.sell_property,name='sell_property'),
    path('rent/',views.rent_property,name='rent_property'),
    path('buy/',views.buy_property,name='buy_property'),
    path('rental_property_view/', views.rental_property_view, name='rental_property_view'),
    path('property_requst_view/', views.property_requst_view, name='property_requst_view'),
]