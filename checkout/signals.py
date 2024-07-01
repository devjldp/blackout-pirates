from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderConcertItem


@receiver(post_save, sender=OrderConcertItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on concertitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderConcertItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on concertitem delete
    """
    instance.order.update_total()
