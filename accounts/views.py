from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_mail(
                subject="Your Verification Code",
                message=f"Your verification code is {user.verification_code}",
                from_email="polpogardner@gmail.com",
                recipient_list=[user.email],
            )
            return Response({"message": "Verification code sent to your email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyAccountView(generics.GenericAPIView):
    def get(self, request, code, *args, **kwargs):
        user = get_object_or_404(CustomUser, verification_code=code)
        if user.email_verified:
            return Response({"message": "Account already verified."}, status=status.HTTP_400_BAD_REQUEST)
        user.email_verified = True
        user.save()
        return Response({"message": "Account verified successfully."}, status=status.HTTP_200_OK)
    
class VerifyCodeView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        # Log the received email and code for debugging
        print("Received email:", email)
        print("Received code:", code)

        # Retrieve the user based on email and verification code
        try:
            user = CustomUser.objects.get(email=email, verification_code=code)
        except CustomUser.DoesNotExist:
            return Response({"error": "Invalid verification code or email."}, status=status.HTTP_400_BAD_REQUEST)

        if user.email_verified:
            return Response({"message": "Account already verified."}, status=status.HTTP_400_BAD_REQUEST)

        # Mark the user as verified
        user.email_verified = True
        user.verification_code = None  # Clear the code after verification
        user.save()

        return Response({"message": "Account verified successfully."}, status=status.HTTP_200_OK)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)  # Ensure this line is correct
        return Response({
            "token": token.key,
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)