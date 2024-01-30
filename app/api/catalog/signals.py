from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Product
from .task import send_mails_about_favourites


@receiver(pre_save, sender=Product)
def added_product(sender, instance, *args, **kwargs):
    try:
        old_instance = Product.objects.get(pk=instance.pk)
        if old_instance.quantity == 0 and instance.quantity != 0:
            send_mails_about_favourites.delay(instance.pk)
    except Product.DoesNotExist:
        pass
