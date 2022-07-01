from celery import shared_task
from transactions.models import Transactions


@shared_task
def scheduled_create(data_list, sender_user):
    try:
        Transactions.objects.create(sender_user_id=sender_user, **data_list)
        msg = "success"
    except Exception as e:
        msg = "error"
    return msg
