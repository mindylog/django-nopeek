"""Test Django Setting Module"""

INSTALLED_APPS = ("nopeek",)

NOPEEK_SETTINGS = {
    "CIPHER_CLASS": "nopeek.crypto.DefaultCipher",
    "CIPHER_TEMPLATE": "AES256_GCM",
    "KEYSET_PATH": "./keyset.json",
}
