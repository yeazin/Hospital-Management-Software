from django.apps import AppConfig


class SadminConfig(AppConfig):
    name = 'sadmin'
    
    def ready(self):
        import sadmin.signals
