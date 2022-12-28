from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from accounts.serializers.register import RegisterSerializer

UserModel = get_user_model()

class RegisterAPIView(CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
