from django.db import models
from django.conf import settings
from base.base_models import BaseModel
from base.constants import OUTGOING, INCOMING


class Transactions(BaseModel):

    TRANSACTION_STATUS_CHOICES = (
        (OUTGOING, "OUTGOING"),
        (INCOMING, "INCOMING"),
    )

    sender_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name="send_transactions")
    receiver_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name="received_transactions")
    status = models.PositiveSmallIntegerField(choices=TRANSACTION_STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ["sender_user", "receiver_user"]
        verbose_name = "Transactions"
        verbose_name_plural = "Transactions"

