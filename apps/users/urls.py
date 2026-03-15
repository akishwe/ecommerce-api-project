from django.urls import path
from apps.users.views.auth_views import LoginAPIView, RegisterUserAPIView, UserProfileAPIView

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
]