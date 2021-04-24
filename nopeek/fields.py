"""nopeek fields."""
from django.db import models
from tink import tink_config


class TinkWrapper:
    """TinkWrapper"""

    def __init__(self) -> None:
        tink_config.register()


class EncryptedFieldMixin:
    """EncrytedFieldMixin."""


class EncryptedCharField(EncryptedFieldMixin, models.CharField):
    """Encyrpted CharField"""


class EncryptedTextField(EncryptedFieldMixin, models.CharField):
    """EncryptedTextField"""


class EncryptedEmailField(EncryptedFieldMixin, models.EmailField):
    """EncryptedTextField"""
