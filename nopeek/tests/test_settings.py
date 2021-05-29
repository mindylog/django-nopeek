"""Test Django Setting Module"""
from pathlib import Path

INSTALLED_APPS = ("nopeek",)

NOPEEK_SETTINGS = {
    "CIPHER_CLASS": "nopeek.crypto.KMSClientCipher",
    "CIPHER_TEMPLATE": "AES256_GCM",
    "KEY_URI": "aws-kms://arn:aws:kms:us-east-2:235739564943:key/3ee50705-5a82-4f5b-9753-05c4f473922f",
    "KMS_CREDENTIALS": str(Path(__file__).resolve().parent.joinpath("test_aws_credentials.txt")),
}
