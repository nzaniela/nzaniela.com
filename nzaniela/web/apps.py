from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'nzaniela.web'
    verbose_name = "WebApp"

    def ready(self):
        pass
