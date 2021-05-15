from django.urls import path
from .views import *
urlpatterns = [
    path('user/', UserAPi.as_view(), name='user'),
    path('persona/', PersonaList.as_view(), name='persona_list'),

]
