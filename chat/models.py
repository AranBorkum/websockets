from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer

from django.db.models.signals import post_save
from django.dispatch import receiver

class TransactionModel(models.Model):
    tx_id = models.CharField(max_length=10)


def update_clients(tx):
    channel_layer = get_channel_layer()
    print(tx.tx_id)
    async_to_sync(channel_layer.group_send)(
        '123',
        {"type": "transaction_updated", "payload": "heyyy"},
    )

@receiver(post_save, sender=TransactionModel, dispatch_uid='update_tx_listeners')
def update_job_status_listeners(sender, instance, **kwargs):
    '''
    Sends job status to the browser when a TransactionModel is modified
    '''
    print("POST SAVE SIGNAL RECEIVED")
    update_clients(instance)
