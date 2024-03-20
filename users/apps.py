from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    # Register signals here. rather than settings.py
    def ready(self) -> None:
        import users.signals