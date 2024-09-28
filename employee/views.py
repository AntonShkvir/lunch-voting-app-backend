from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Employee
from .serializers import EmployeeSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        employees = self.get_queryset()
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data)


class EmployeeRegisterView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class EmployeeLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=400)
