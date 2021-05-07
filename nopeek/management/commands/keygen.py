"""Django manage.py command for create keyset handle"""
from typing import Any, Optional

import tink
from django.core.management.base import BaseCommand, CommandError, CommandParser
from tink import cleartext_keyset_handle, tink_config

from ._enums import TinkTemplate


class Command(BaseCommand):
    """Keyset Generate command"""

    help = "Generate keyset file for using Cipher module"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add keygen arguments"""
        parser.add_argument(
            "key_path", type=str, help="Where the key will be stored and What is the key name"
        )
        parser.add_argument("--template", type=str, help="Template for keyset", default="AES128_GCM")

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """Execute command"""

        template_enum = options["template"].upper()

        try:
            module_name, template_root, template_name = TinkTemplate[template_enum]
        except KeyError:
            raise CommandError(f"Template {template_enum} is not exists.")
        try:
            module = getattr(tink, module_name)
            tink_config.register()
        except tink.TinkError as e:
            raise CommandError(f"Error initialising Tink: {e}")

        try:
            key_template = getattr(getattr(module, template_root), template_name)
            keyset_handle = tink.KeysetHandle.generate_new(key_template)
        except tink.TinkError as e:
            raise CommandError(f"Error creating primitive: {e}")

        location = options["key_path"]
        with open(location, "wt") as keyset_file:
            try:
                cleartext_keyset_handle.write(tink.JsonKeysetWriter(keyset_file), keyset_handle)
            except tink.TinkError as e:
                raise CommandError(f"Error writing key: {e}")

        self.stdout.write(self.style.SUCCESS(f"Successfully generate key to {location}"))
