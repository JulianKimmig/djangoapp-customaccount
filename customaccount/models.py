from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"),on_delete=models.SET_NULL,null=True)
    deleted = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    public_name= models.CharField(max_length=20,verbose_name=_("Public Name"))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.get()
        CustomUser.objects.create(user=instance,public_name=(instance.first_name + " " + instance.last_name if len(instance.first_name) > 0 and len(instance.last_name) > 0 else instance.username))

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    CustomUser.objects.get(user=instance).save()
#    instance.custom_user.save()