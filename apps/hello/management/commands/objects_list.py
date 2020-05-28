from django.db import models
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        models_list = models.get_models()
        for model in models_list:
            count = model.objects.count()
            print("{0} has {1} objects".format(model, count))
