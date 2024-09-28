from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        restaurants = self.get_queryset()
        serializer = self.get_serializer(restaurants, many=True)
        return Response(serializer.data)
