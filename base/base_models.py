from django.db import models
from accounts.models import User


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, db_index=True, editable=False,
                                   on_delete=models.SET_NULL, related_name="%(class)s_created")
    updated_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, null=True, db_index=True, editable=False,
                                   on_delete=models.SET_NULL, related_name="%(class)s_updated")
