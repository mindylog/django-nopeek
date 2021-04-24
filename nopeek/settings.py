"""django nopeek setting.

In settings.py,

NOPEEK_SETTINGS = {
    "CIPHER_MODULE": "tink.daead",
    "KMS_INTEGRATION_CLIENT": "tink.integration.gcpkms.GcpKmsClient",
}
"""

from django.conf import settings

from .utils import import_callable

DEFAULT_SETTINGS = {
    "CIPHER_MODULE": import_callable("tink.aead"),
    "KMS_INTEGRATION_CLIENT": None,
}

nopeek_settings = getattr(settings, "NOPEEK_SETTINGS", DEFAULT_SETTINGS)
