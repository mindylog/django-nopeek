"""Test Django Setting Module"""

INSTALLED_APPS = ("nopeek",)

NOPEEK_SETTINGS = {
    "CIPHER_MODULE": "tink.aead",
    "CREDENTIAL_PATH": "/app/mypath/keyset.json",
    "CIPHER_PRIMITIVE": "Aead",
}
