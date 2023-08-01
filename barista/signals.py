from django.db.models.signals import post_save
from django.dispatch import receiver

from warehouse.models import ReadyProducts
from .models import Order


@receiver(post_save, sender=Order)
def update_products_on_order_create(sender, instance, created, **kwargs):
    if created:
        order_contents = instance.order_contents.all()

        for menu_item in order_contents:
            menu_item.quantity -= 1
            menu_item.save()

        ready_products = ReadyProducts.objects.filter(menu_item__in=order_contents)
        for ready_product in ready_products:
            ready_product.quantity -= 1
            ready_product.save()
