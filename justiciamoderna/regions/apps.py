"""Region Config"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RegionConfig(AppConfig):
    name = "justiciamoderna.regions"
    verbose_name = _("Regions")

    def ready(self):
        try:
            import justiciamoderna.regions.signals  # noqa F401
        except ImportError:
            pass
