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
