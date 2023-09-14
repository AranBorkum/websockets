import uuid
from datetime import datetime

from django.db import models
from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer

from django.db.models.signals import post_save
from django.dispatch import receiver


class TransactionModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    information = models.JSONField(default=dict)


def update_clients(tx):
    channel_layer = get_channel_layer()
    print(tx.id)
    async_to_sync(channel_layer.group_send)(
        str(tx.id),
        {
            "type": "transaction_updated",
            "timestamp": str(datetime.now()),
            "message": f"Updated transaction {tx.id}",
        },
    )


@receiver(post_save, sender=TransactionModel, dispatch_uid="update_tx_listeners")
def update_job_status_listeners(sender, instance, **kwargs):
    print("POST SAVE SIGNAL RECEIVED")
    update_clients(instance)
