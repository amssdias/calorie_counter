from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView, PasswordResetView

from .views import CustomLoginView, ProfileView, RegisterView, ActivateAccountView

app_name = "accounts"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", include([
        path("", CustomLoginView.as_view(), name='login'),
        path("activate_account/<str:uidb64>/<str:token>", ActivateAccountView.as_view(), name="activate_account"),
    ])),
    path("forgot-password/", PasswordResetView.as_view(), name="password_reset"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path('<uuid:uuid>/', ProfileView, name="main"),
    # path('', RedirectView.as_view(url="login")),
]

