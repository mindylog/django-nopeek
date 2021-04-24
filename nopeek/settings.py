"""Settings"""

from django.conf import settings

# NOTE: Please add default setting
DEFAULT = {}

nopeek_settings = getattr(settings, "NOPEEK_SETTING", DEFAULT)
