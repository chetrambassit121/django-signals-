from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

















# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save  
# # Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     first_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200, null=True, blank=True)
#     phone = models.CharField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return str(self.user)


# def create_profile(sender, instance, created, **kwargs):

#     if created:
#         Profile.objects.create(user=instance)
#         print('Profile created')

# # when a user is created so is a profile .. username (user) shown on admin/profiles

# post_save.connect(create_profile, sender=User)


# def update_profile(sender, instance, created, **kwargs):

#     if created == False:
#         instance.profile.save()
#         print('profile updated')

# post_save.connect(create_profile, sender=User)

















# from django.db import models
# from django.contrib.auth.models import User 
# # Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     first_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200, null=True, blank=True)
#     phone = models.CharField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return self.first_name


# # def create_profile():


# # def update_profile():