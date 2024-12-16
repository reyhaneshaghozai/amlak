from django.urls import path
from .views import collect_phone_number,verify_otp

app_name = 'authentication'

urlpatterns = [
    path('', collect_phone_number, name='collect_phone_number'),
    path('verify-otp/<str:phone_number>/', verify_otp, name='verify_otp'),   
]
