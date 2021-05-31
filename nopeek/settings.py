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
    "CIPHER_CLASS": "nopeek.crypto.DefaultCipher",
    "CIPHER_TEMPLATE": "AES128_GCM",
    "KEYSET_PATH": None,
    "CYPHERTEXT_PREFIX": None,
}

nopeek_settings = getattr(settings, "NOPEEK_SETTINGS", DEFAULT_SETTINGS)
