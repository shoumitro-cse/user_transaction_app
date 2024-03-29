from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    """
    An abstract base class implements a fully featured to identify while a user
    occurs any action like creating or updating a database table record.
    """

    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, db_index=True, editable=False,
                                   on_delete=models.SET_NULL, related_name="%(class)s_created")
    updated_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, db_index=True, editable=False,
                                   on_delete=models.SET_NULL, related_name="%(class)s_updated")
