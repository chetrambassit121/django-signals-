from django.db.models.signals import post_save 
from django.db.models.signals import pre_save 
from django.dispatch import receiver 
# from django.contrib.auth.models import User 
from buyers.models import Buyer
from .models import Car
import uuid

@receiver(pre_save, sender=Car)
def pre_save_modify_buyer_and_create_code(sender, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]       # will give us a unique code for each car 

    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()