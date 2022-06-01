from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

def pre_save_post(sender, instance, **kwargs):
    print('success with pre_save signal') 

def save_post(sender, instance, **kwargs):
    print('success with post_save signal') 

def after_delete_post(sender, instance, **kwargs):
    print('success with post_delete signal')

pre_save.connect(pre_save_post, sender=Post) 
post_save.connect(save_post, sender=Post) 
post_delete.connect(after_delete_post, sender=Post)














# from django.db import models
# from django.db.models.signals import pre_save, post_save, post_delete

# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

# def pre_save_post(sender, instance, **kwargs):
#     print('success with pre_save signal') 

# def save_post(sender, instance, **kwargs):
#     print('success with post_save signal') 

# def after_delete_post(sender, instance, **kwargs):
#     print('success with post_delete signal')

# pre_save.connect(pre_save_post, sender=Post) 
# post_save.connect(save_post, sender=Post) 
# post_delete.connect(after_delete_post, sender=Post)



# # >>> from posts.models import Post
# # >>> p = Post.objects.first()
# # >>> p.delete()
# # success with post_delete signal
# # (1, {'posts.Post': 1})
# # >>>

# # deleted the first post 















# from django.db import models
# from django.db.models.signals import pre_save, post_save

# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

# def pre_save_post(sender, instance, **kwargs):
#     print('success with pre_save signal') 

# def save_post(sender, instance, **kwargs):
#     print('success with post_save signal') 

# pre_save.connect(pre_save_post, sender=Post) 
# post_save.connect(save_post, sender=Post) 



# # >>> from posts.models import Post
# # >>> p3 = Post()
# # >>> p3.title = ' third title ' 
# # >>> p3.save()
# # success with signal           # this is the pre_save signal 
# # success with signal           # this is the post_save signal
# # >>>














# from django.db import models
# from django.db.models.signals import pre_save, post_save

# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

# def save_post(sender, instance, **kwargs):
#     print('success with signal') 

# post_save.connect(save_post, sender=Post) 


# # >>> from posts.models import Post
# # >>> p = Post.objects.create(title='first post')
# # success with signal
# # >>>



# # >>> p2 = Post()                                 
# # >>> p2.title = 'second title'
# # >>> p2.save()
# # success with signal
# # >>>