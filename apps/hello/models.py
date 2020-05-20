from django.db import models


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
