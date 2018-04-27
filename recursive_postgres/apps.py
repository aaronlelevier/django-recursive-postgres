from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HMACConfig(AppConfig):
    name = 'recursive_postgres'
    verbose_name = _("Django Recursive Postgres")
