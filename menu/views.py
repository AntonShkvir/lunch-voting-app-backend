from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from vote.models import Vote
from .models import Menu
from .serializers import MenuSerializer, MenuDetailSerializer
from django.utils import timezone
from django.db.models import Max, Count

class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        current_time = timezone.now().time()

        current_day_menu = self.queryset.filter(date=today)

        # shows most voted lunch after 13:00 (lunchtime)
        if current_time > timezone.datetime.strptime('4:00', '%H:%M').time():
            max_votes = Vote.objects.filter(menu__in=current_day_menu).values('menu').annotate(vote_count=Count('id')).aggregate(
                Max('vote_count'))['vote_count__max']

            if max_votes:
                current_day_menu = current_day_menu.filter(
                    id__in=Vote.objects.filter(menu__in=current_day_menu).values('menu').annotate(
                        vote_count=Count('id')).filter(vote_count=max_votes).values('menu')
                )


        serializer = self.get_serializer(current_day_menu, many=True)
        for menu in current_day_menu:
            menu.votes_count = Vote.objects.filter(menu=menu).count()

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        menu_id = request.data.get('menu')
        if Vote.objects.filter(employee=request.user.employee, menu_id=menu_id).exists():
            return Response({'error': 'You have already voted for this menu.'}, status=status.HTTP_400_BAD_REQUEST)

        vote = Vote.objects.create(employee=request.user.employee, menu_id=menu_id)
        return Response({'message': 'Vote submitted successfully.'}, status=status.HTTP_201_CREATED)


class MenuDetailView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        menu_id = kwargs.get('pk')
        try:
            menu = self.get_object()
            serializer = self.get_serializer(menu)
            return Response(serializer.data)
        except Menu.DoesNotExist:
            return Response({'error': 'Menu not found.'}, status=404)
