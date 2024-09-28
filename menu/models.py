from django.db import models
from restaurant.models import Restaurant

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()
    votes_count = 0

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['restaurant', 'date', 'items'], name='unique_menu_items_for_restaurant_per_day')
        ]

    def __str__(self):
        return f"{self.restaurant.name} - {self.date}"
