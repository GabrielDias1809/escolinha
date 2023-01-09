from django.urls import path
from .views import UseRegisterView
urlpatterns = [
    path('register/',UseRegisterView.as_view(), name = "register"),
]