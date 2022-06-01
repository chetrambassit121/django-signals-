from django.db import models
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

def save_post(sender, instance, **kwargs):
    print('success with signal') 

post_save.connect(save_post, sender=Post) 


