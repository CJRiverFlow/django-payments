from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

class User(AbstractUser):
    slug = models.SlugField(max_length=200, null=True, blank=True, default="")

