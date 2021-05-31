"""Exceptions"""
from tink import TinkError


class CipherInitialisationError(TinkError):
    """Cipher register failed exception"""


class InvalidKeyFileError(TinkError):
    """Cipher keyset is invalid exception"""


class WrongPrimitiveError(TinkError):
    """Wrong Primitive Error"""


class EncryptedFieldException(Exception):
    """Encrypted Field base exception"""


class NotSupportModuleError(Exception):
    """Cipher Module is not acceptable"""


class UnknownKMSClientError(Exception):
    """Unknown KMS Client Exception"""


class CredentialNotConfigured(Exception):
    """Credential not configured"""


class KMSRegistrationFailed(Exception):
    """KMS Registration Failed"""


class DetermisticAeadNotSupported(Exception):
    """Daead is not supported"""


class TemplateNotFoundException(Exception):
    """TemplateNotFoundException"""
