from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class AmountValidator(validators.RegexValidator):
    regex = r"^(?!0\d)\d*(\.\d+)?$"
    message = _(
        "Enter a valid amount. This value may contain only float numbers."
    )
    flags = 0


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^(?:(?:\+|00)88|01)?\d{11}$"
    message = _(
        "Enter a valid phone number. This value may contain only numbers."
    )
    flags = 0
