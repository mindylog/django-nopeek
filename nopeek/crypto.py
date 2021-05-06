import abc

import tink

from .exceptions import CipherInitialisationError
from .settings import nopeek_settings
from .utils import import_callable


class BaseCipher:
    """BaseCrypter Class"""

    __metaclass__ = abc.ABCMeta

    def __init__(self) -> None:
        """Base Crypter Class Constructor"""
        try:
            cipher = import_callable(nopeek_settings["CIPHER_MODULE"])
            cipher.register()
        except tink.TinkError:
            raise CipherInitialisationError(
                "Failed when initialising cipher module {}".format(nopeek_settings["CIPHER_MODULE"])
            )

    @abc.abstractmethod
    def encrypt(self) -> None:
        """Encrypt plain text"""
        raise NotImplementedError("Method encrypt is not implemented.")

    @abc.abstractmethod
    def decrypt(self) -> None:
        """Decrypt cipher text"""
        raise NotImplementedError("Method decrypt is not implemented.")


class DefaultCipher(BaseCipher):
    """DefaultCrypter Class"""


class KMSCrypter(BaseCipher):
    """KMSCrypter Class"""
