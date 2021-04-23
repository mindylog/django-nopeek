"""nopeek fields."""
from django.db import models


class EncryptedFieldMixin:
    """EncrytedFieldMixin."""


class EncryptedCharField(EncryptedFieldMixin, models.CharField):
    """Encyrpted CharField"""


class EncryptedTextField(EncryptedFieldMixin, models.CharField):
    """EncryptedTextField"""


class EncryptedEmailField(EncryptedFieldMixin, models.EmailField):
    """EncryptedTextField"""
