from django.urls import path
from .views import collect_phone_number

app_name = 'authentication'

urlpatterns = [
    path('', collect_phone_number, name='collect_phone_number'),
]
