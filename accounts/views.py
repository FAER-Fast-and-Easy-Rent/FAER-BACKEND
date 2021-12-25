from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserSerializer

User = get_user_model()

PASSWORD_LENGTH_ERROR = "Password must me at least 8 characters long."
PASSWORD_MISMATCH = "Passwords do not match."
USER_EXISTS = "User with this email already exists."
MESSAGE = "Something went wrong."
FIELD_MISSING = "Fields are missing."


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data

            if not data:
                return Response({'error': FIELD_MISSING}, status=status.HTTP_400_BAD_REQUEST)
            fields = ['name', 'email', 'password', 're_password']
            message = {field: 'is required.' for field in fields if field not in data}
            if tuple(fields) not in data and message:
                return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)

            name, email, password, re_password = data['name'], data['email'], data['password'], data['re_password']
            email = email.lower()
            if len(password) < 8:
                return Response({'error': PASSWORD_LENGTH_ERROR}, status=status.HTTP_400_BAD_REQUEST)
            if password != re_password:
                return Response({'error': PASSWORD_MISMATCH}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=email).exists():
                return Response({'error': USER_EXISTS}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            User.objects.create_user(email, name, password)
            return Response({'success': "User created successfully."}, status=status.HTTP_201_CREATED)

        except Exception:
            return Response({'error': MESSAGE}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            return Response({'user': user.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': MESSAGE}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)