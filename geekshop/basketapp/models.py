from django.db import models
from django.conf import settings
from mainapp.models import Product

class Basket(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True
    )
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    is_active = models.BooleanField(verbose_name='активна', default=True)


    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filters(user = self.user)
        _total_quantity = sum(list(map(lambda : x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filters(user=self.user)
        _total_cost = sum(list(map(lambda: x.product_cost, _items)))
        return _total_cost

