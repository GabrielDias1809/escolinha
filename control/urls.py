from django.urls import path
from .views import HomeView, Checkin, AddAulaView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('checkin/<int:pk>', Checkin.as_view(), name="checkin" ),
    path('add_aula/',AddAulaView.as_view(), name = "add_aula"),
]