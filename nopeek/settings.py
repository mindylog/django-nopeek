"""django nopeek setting.

In settings.py,

NOPEEK_SETTINGS = {
    "CIPHER_MODULE": "tink.aead",
    "CREDENTIAL_PATH": "/app/mypath/keyset.json",
    "CIPHER_PRIMITIVE": "Aead",
}
"""

from django.conf import settings

DEFAULT_SETTINGS = {
    "CIPHER_MODULE": "tink.aead",
    "CREDENTIAL_PATH": None,
    "CIPHER_PRIMITIVE": "Aead",
    "KEYSET_PATH": None,
}

nopeek_settings = getattr(settings, "NOPEEK_SETTINGS", DEFAULT_SETTINGS)
