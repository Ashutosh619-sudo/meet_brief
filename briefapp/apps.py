from django.apps import AppConfig


class BriefappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'briefapp'

    def ready(self) -> None:
        super(BriefappConfig,self).ready()
        from . import signals
