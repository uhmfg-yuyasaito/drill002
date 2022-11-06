# signalを発火させるための設定
from django.apps import AppConfig

class UhdrillConfig(AppConfig):
    name = 'uhdrill'

    def ready(self):
        from . import signal