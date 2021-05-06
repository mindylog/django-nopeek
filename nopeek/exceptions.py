"""Exceptions"""
from tink import TinkError


class CipherInitialisationError(TinkError):
    """Cipher register failed exception"""


class InvalidKeyFileError(TinkError):
    """Cipher keyset is invalid exception"""


class EncryptedFieldException(Exception):
    """Encrypted Field base exception"""
