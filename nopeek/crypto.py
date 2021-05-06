import abc
from typing import Any

import tink
from tink import cleartext_keyset_handle

from .exceptions import CipherInitialisationError, InvalidKeyFileError
from .settings import nopeek_settings
from .utils import import_callable


class BaseCipher:
    """BaseCipher Class"""

    __metaclass__ = abc.ABCMeta

    def __init__(self) -> None:
        """Base Cipher Class Constructor"""
        try:
            module = import_callable(nopeek_settings["CIPHER_MODULE"])
            module.register()
            self.module = module
        except tink.TinkError:
            raise CipherInitialisationError(
                "Failed when initialising cipher module {}".format(nopeek_settings["CIPHER_MODULE"])
            )

    @abc.abstractmethod
    def encrypt(self, input_data: Any, associated_data: str) -> str:
        """Encrypt plain text"""
        raise NotImplementedError("Method encrypt is not implemented.")

    @abc.abstractmethod
    def decrypt(self, input_data: Any, associated_data: str) -> str:
        """Decrypt cipher text"""
        raise NotImplementedError("Method decrypt is not implemented.")


class DefaultCipher(BaseCipher):
    """DefaultCipher Class"""

    def __init__(self) -> None:
        super().__init__()
        with open(nopeek_settings["CREDENTIAL_PATH"]) as keyset_file:
            try:
                text = keyset_file.read()
                keyset_handle = cleartext_keyset_handle.read(tink.JsonKeysetReader(text))
            except tink.TinkError as e:
                raise InvalidKeyFileError(f"Error reading key: {e}")
        self.cipher = keyset_handle.primitive(getattr(self.module, nopeek_settings["CIPHER_PRIMITIVE"]))

    def encrypt(self, input_data: bytes, associated_data: bytes) -> bytes:
        return self.cipher.encrypt(input_data, associated_data)

    def decrypt(self, input_data: bytes, associated_data: bytes) -> bytes:
        return self.cipher.decrypt(input_data, associated_data)


class KMSClientCipher(BaseCipher):
    """KMSCipher Class"""
