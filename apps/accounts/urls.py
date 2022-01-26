from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, ProfileView, RegisterView, ActivateAccountView


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', include([
        path('', CustomLoginView.as_view(), name='login'),
        path('activate_account/<str:uidb64>/<str:token>', ActivateAccountView.as_view(), name="activate_account"),
        # path('forgot-password/', PasswordResetView, name="password_reset"),
    ])),
    path('profile/', ProfileView.as_view(), name="main"),
    path('logout', LogoutView.as_view(next_page="login"), name="logout"),
    # path('<uuid:uuid>/', ProfileView, name="main"),
    # path('', RedirectView.as_view(url="login")),
]

