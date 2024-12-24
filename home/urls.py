from django.urls import path
from. import views


urlpatterns = [
    path('',views.home,name='home'),
    path('sell/',views.sell_property,name='sell_property'),
    path('rent/',views.rent_property,name='rent_property'),
    path('buy/',views.buy_property,name='buy_property'),
]