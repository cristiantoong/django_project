from django.db.models.signals import post_save
from django.contrib.auth.models import User  # sender, sending the signal
from django.dispatch import receiver
from .models import Profile

# when the user is saved send the 'post_save' signal and the signal is going to be received by the create_profile receiver
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # create(title='',content='')


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # user.profile.save()
