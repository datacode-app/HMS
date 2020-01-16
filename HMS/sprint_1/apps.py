from django.apps import AppConfig


class Sprint1Config(AppConfig):
    name = 'sprint_1'
    def ready(): #updater
        from . import update
        update.daily_check()
