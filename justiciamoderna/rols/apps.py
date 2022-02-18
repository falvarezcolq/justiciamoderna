"""Rol Config"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RolConfig(AppConfig):
    name = "justiciamoderna.rols"
    verbose_name = _("Rols")

    def ready(self):
        try:
            import justiciamoderna.rols.signals  # noqa F401
        except ImportError:
            pass
