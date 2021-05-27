from django.urls import path
from . import views

#empty string represents root of this app... trades/
#Possible endpoint structure:
#trades/ (root '')
#trades/05-27-2021/
#trades/05-27-2021/closed
urlpatterns = [
    path('', views.index, name='index')
]
