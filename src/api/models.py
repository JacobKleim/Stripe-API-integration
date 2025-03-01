from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Item {self.id} {self.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def calculate_total_price(self):
        """Расчитывает стоимость товаров в заказе"""
        total = sum(item.price for item in self.items.all())
        return total

    def __str__(self):
        return f'Order {self.id} for {self.user.username}'
