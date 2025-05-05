from django.urls import path
from .views import RegisterView, LoginView, VerifyAccountView, VerifyCodeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/<uuid:code>/', VerifyAccountView.as_view(), name='verify-account'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),  # Add this line
]