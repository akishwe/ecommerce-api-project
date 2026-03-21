from django.urls import path
from apps.users.views.auth_views import (
    RegisterUserAPIView,
    LoginAPIView,
    UserProfileAPIView,
    UserAddressListCreateAPIView,
    UserAddressRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("addresses/", UserAddressListCreateAPIView.as_view(), name="addresses"),
    path("addresses/<int:pk>/", UserAddressRetrieveUpdateDestroyAPIView.as_view(), name="address-detail"),
]