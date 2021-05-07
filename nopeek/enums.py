"""Private Module Enums"""

from enum import Enum


class TinkTemplate(tuple, Enum):
    """Tink Template Enum Class"""

    AES128_EAX = ("aead", "aead_key_templates", "AES128_EAX")
    AES256_EAX = ("aead", "aead_key_templates", "AES256_EAX")
    AES128_GCM = ("aead", "aead_key_templates", "AES128_GCM")
    AES256_GCM = ("aead", "aead_key_templates", "AES256_GCM")
    AES128_GCM_SIV = ("aead", "aead_key_templates", "AES128_GCM_SIV")
    AES256_GCM_SIV = ("aead", "aead_key_templates", "AES256_GCM_SIV")
    AES256_SIV = ("daead", "deterministic_aead_key_templates", "AES256_SIV")
    AES128_CTR_HMAC_SHA256 = ("aead", "aead_key_templates", "AES128_CTR_HMAC_SHA256")
    AES256_CTR_HMAC_SHA256 = ("aead", "aead_key_templates", "AES256_CTR_HMAC_SHA256")
    XCHACHA20_POLY1305 = ("aead", "aead_key_templates", "XCHACHA20_POLY1305")
