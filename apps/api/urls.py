from django.urls import path
from .views import UserAPi
urlpatterns = [
    path('user/', UserAPi.as_view(), name='user'),
]
