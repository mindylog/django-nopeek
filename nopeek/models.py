from django.db import models

from .settings import settings as nopeek_settings
from .utils import import_callable


class EncrpytedModelMixin(models.Model):
    """Nopeek Encrpyted Model Mixin

    Args:
        models (django.db.models): Django Model
    """

    cipher_module = import_callable(nopeek_settings["CIPHER_CLASS"])

    class Meta:
        """Metaclass"""

        abstract = True
