import abc
from typing import Any

import tink
from tink import TinkError, aead, cleartext_keyset_handle, tink_config
from tink.integration import awskms, gcpkms

from nopeek.enums import KMSScheme, TinkTemplate
from nopeek.exceptions import (
    CipherInitialisationError,
    CredentialNotConfigured,
    DetermisticAeadNotSupported,
    InvalidKeyFileError,
    KMSRegistrationFailed,
    NotSupportModuleError,
    TemplateNotFoundException,
    UnknownKMSClientError,
    WrongPrimitiveError,
)
from nopeek.settings import nopeek_settings
from nopeek.utils import scheme


class BaseCipher:
    """BaseCipher Class"""

    __metaclass__ = abc.ABCMeta

    def __init__(self) -> None:
        """Base Cipher Class Constructor"""
        try:
            template_name = nopeek_settings["CIPHER_TEMPLATE"]
            module_name, template_root, template = TinkTemplate[template_name]
        except KeyError:
            raise KeyError("Invalid or unset template. Please use valid CIPHER_TEMPLATE.")
        try:
            module = getattr(tink, module_name)
            tink_config.register()
            self.module_name = module_name
            self.module = module
            self.template_root = template_root
            self.template = template
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
        with open(nopeek_settings["KEYSET_PATH"]) as keyset_file:
            try:
                text = keyset_file.read()
                keyset_handle = cleartext_keyset_handle.read(tink.JsonKeysetReader(text))
            except tink.TinkError as e:
                raise InvalidKeyFileError(f"Error reading key: {e}")

        primitive = "Aead"

        if self.module_name == "daead":
            primitive = "DeterministicAead"
        try:
            self.cipher = keyset_handle.primitive(getattr(self.module, primitive))
        except TinkError as e:
            raise WrongPrimitiveError(f"Error initialisation with {e}")

    def encrypt(self, input_data: bytes, associated_data: bytes) -> bytes:
        if self.module_name == "aead":
            return self.cipher.encrypt(input_data, associated_data)
        elif self.module_name == "daead":
            return self.cipher.encrypt_deterministically(input_data, associated_data)
        else:
            raise NotSupportModuleError("Only can use few encryption module(aead, daead).")

    def decrypt(self, input_data: bytes, associated_data: bytes) -> bytes:
        if self.module_name == "aead":
            return self.cipher.decrypt(input_data, associated_data)
        elif self.module_name == "daead":
            return self.cipher.decrypt_deterministically(input_data, associated_data)
        else:
            raise NotSupportModuleError("Only can use few encryption module(aead, daead).")


class KMSClientCipher(BaseCipher):
    """KMSCipher Class"""

    def __init__(self) -> None:
        super().__init__()

        if self.module_name == "daead":
            raise DetermisticAeadNotSupported()

        key_uri = nopeek_settings.get("KEY_URI")

        if (not key_uri) or (scheme(key_uri) not in KMSScheme._value2member_map_):  # pylint: disable=E1101
            raise UnknownKMSClientError()

        if not nopeek_settings.get("KMS_CREDENTIALS"):
            raise CredentialNotConfigured()

        scheme_type = KMSScheme(scheme(key_uri))

        try:
            if scheme_type == KMSScheme.GCP:
                self.client = gcpkms.GcpKmsClient(key_uri, nopeek_settings["KMS_CREDENTIALS"])
            else:
                self.client = awskms.AwsKmsClient(key_uri, nopeek_settings["KMS_CREDENTIALS"])

            cloud_aead = self.client.get_aead(key_uri)

        except TinkError as e:
            raise KMSRegistrationFailed(e)

        try:
            key_template = getattr(getattr(self.module, self.template_root), self.template)
        except AttributeError:
            raise TemplateNotFoundException()
        self.cipher = aead.KmsEnvelopeAead(key_template, cloud_aead)

    def encrypt(self, input_data: bytes, associated_data: bytes) -> bytes:
        return self.cipher.encrypt(input_data, associated_data)

    def decrypt(self, input_data: bytes, associated_data: bytes) -> bytes:
        return self.cipher.decrypt(input_data, associated_data)
