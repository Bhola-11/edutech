from django.contrib import admin
from . import models

# Register all models in app
for name, cls in models.__dict__.items():
    if isinstance(cls, type) and issubclass(cls, models.models.Model) and not cls._meta.abstract:
        try:
            admin.site.register(cls)
        except admin.sites.AlreadyRegistered:
            pass
