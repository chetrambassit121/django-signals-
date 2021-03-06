from django.db.models.signals import post_save  
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile 





@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        print('Profile created')

# when a user is created so is a profile .. username (user) shown on admin/profiles

post_save.connect(create_profile, sender=User)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created == False:
        instance.profile.save()
        print('profile updated')

post_save.connect(create_profile, sender=User)