from django.db import models
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        models_list = models.get_models()
        for model in models_list:
            count = model.objects.count()
            output_str = "{0} has {1} objects".format(model, count)
            print(output_str)
        for model in models_list:
            count = model.objects.count()
            output_str = "{0} has {1} objects".format(model, count)
            self.stderr.write('error: ' + output_str)
