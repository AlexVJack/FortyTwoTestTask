from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save


class PersonInfo(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_bearth = models.CharField(max_length=120)
    bio = models.TextField()
    email = models.CharField(max_length=120)
    jabber = models.CharField(max_length=120)
    skype = models.CharField(max_length=120)
    other_contacts = models.TextField()

    def __unicode__(self):
        return self.name


class HttpRequestModel(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50)
    path = models.CharField(max_length=1000)

    def total_requests(self):
        return len(HttpRequestModel.objects.all())


class DbActions(models.Model):
    time = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=100)
    action_type = models.CharField(max_length=50)


# should write main_models inside a function
# cause tests don't like functions with a single if
@receiver(post_save)
def create_edit_case(sender, created, **kwargs):
    "Writes entry to db in case of create or edit operation"
    main_models = ['PersonInfo', 'HttpRequestModel']
    if sender.__name__ in main_models:
        if created:
            DbActions.objects.create(model=sender.__name__,
                                     action_type='has been created')
        else:
            DbActions.objects.create(model=sender.__name__,
                                     action_type="has been edited")


@receiver(post_delete)
def delete_case(sender, **kwargs):
    "Writes entry to db in case of delete operation"
    main_models = ['PersonInfo', 'HttpRequestModel']
    if sender.__name__ in main_models:
        DbActions.objects.create(model=sender.__name__,
                                 action_type="has been deleted")
