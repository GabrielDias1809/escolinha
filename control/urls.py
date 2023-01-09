from django.urls import path
from .views import HomeView, Checkin, AddAulaView, UpdateAulaView, DeleteAulaView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('checkin/<int:pk>', Checkin.as_view(), name="checkin" ),
    path('add_aula/',AddAulaView.as_view(), name = "add_aula"),
    path('aula/edit/<int:pk>', UpdateAulaView.as_view(), name = "update_aula"),
    path('aula/delete/<int:pk>', DeleteAulaView.as_view(), name = "delete_aula"),
]