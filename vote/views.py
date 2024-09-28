from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Vote
from .serializers import VoteSerializer

from menu.models import Menu
from employee.models import Employee


class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        menu_id = self.request.data.get('menu')
        try:
            menu = Menu.objects.get(id=menu_id)
        except Menu.DoesNotExist:
            return Response({'error': 'Menu not found.'}, status=status.HTTP_404_NOT_FOUND)
        try:
            employee = Employee.objects.get(user=self.request.user)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found.'}, status=status.HTTP_404_NOT_FOUND)
        if Vote.objects.filter(employee=employee, menu=menu).exists():
            return Response({'error': 'You have already voted for this menu.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(employee=employee, menu=menu)
        menu.votes_count += 1
        menu.save()
