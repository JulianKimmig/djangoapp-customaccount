from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUser(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"),on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    public_name= models.CharField(max_length=20,verbose_name=_("Public Name"))
