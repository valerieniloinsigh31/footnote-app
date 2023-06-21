from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import FootNote


@receiver(post_save, sender=FootNoteLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update footnote total on lineitem update/create
    """
    instance.footnote.update_total()


@receiver(post_delete, sender=FootNoteLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update footnote total on lineitem delete
    """
    print('delete signal received')
    instance.footnote.update_total()