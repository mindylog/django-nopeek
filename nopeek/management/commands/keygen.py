"""Django manage.py command for create keyset handle"""
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    """Keyset Generate command"""

    help = "Generate keyset file for using Cipher module"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add keygen arguments"""
        parser.add_argument("keyset_path", nargs=1, type=str)

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """Execute command"""
