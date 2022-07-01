from django.db import models
from django.conf import settings
from base.base_models import BaseModel
from base.validators import AmountValidator


class Transactions(BaseModel):
    """
    Here, we can store user transaction information and easily find out a user transaction.
    """

    AmountValidator = AmountValidator()
    sender_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name="send_transactions")
    receiver_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name="received_transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[AmountValidator])

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

