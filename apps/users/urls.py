from django.urls import path
from apps.users.views.auth_views import RegisterUserAPIView

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
]