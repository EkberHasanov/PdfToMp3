from django.urls import path
from accounts.views import RegisterAPIView

urlpatterns = [
    path('sign-up/', RegisterAPIView.as_view(), name='sign-up'),
]
