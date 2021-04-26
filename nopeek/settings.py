"""django nopeek setting.

In settings.py,

NOPEEK_SETTINGS = {
    "CIPHER_MODULE": "tink.daead",
    "KMS_INTEGRATION_CLIENT": "tink.integration.gcpkms.GcpKmsClient",
    "KEYSET_PATH": "gcp-kms://projects/tink-examples/locations/global/keyRings/foo/cryptoKeys/bar",
}
"""

from django.conf import settings

DEFAULT_SETTINGS = {
    "CIPHER_MODULE": "tink.aead",
    "KMS_INTEGRATION_CLIENT": None,
    "KEYSET_PATH": None,
}

nopeek_settings = getattr(settings, "NOPEEK_SETTINGS", DEFAULT_SETTINGS)
