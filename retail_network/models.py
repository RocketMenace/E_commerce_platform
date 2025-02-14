from django.db import models
from contacts.models import Contact

# Create your models here.


class NetworkNode(models.Model):
    title = models.CharField(max_length=200, verbose_name="название")
    contacts = models.ManyToManyField(Contact, related_name="", verbose_name="контакты")
