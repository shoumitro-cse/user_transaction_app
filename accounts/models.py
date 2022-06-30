from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^(?:(?:\+|00)88|01)?\d{11}$"
    message = _(
        "Enter a valid phone number. This value may contain only numbers."
    )
    flags = 0


class User(AbstractUser):
    """
    This class has a set of defined attributes (characteristics) and
    methods (behaviors) that you can use to refer to multiple data items
    as a single entity. also, we can store all users.
    """

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("Phone number"),
        max_length=15,
        unique=True,
        help_text=_(
            "Required. 15 numbers or fewer. digits and + only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that phone number already exists."),
        },
    )
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    """
    Here, we can store user profile information separately.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    profile_image = models.ImageField(default='default.png', upload_to='images/profile/')
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username
