from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

def post_student_save(sender, instance, **kwargs):
    print("your post has been saved")

def post_student_delete(sender, instance, **kwargs):
    print("your post has been deleted")


post_save.connect(post_student_save, Student)
pre_save.connect(post_student_save, Student)           
post_delete.connect(post_student_delete, Student)

# shell 

# >>> from app.models import Student 
# >>> p4 = Student.objects.first()
# >>> p4.delete()
# your post has been deleted
# (1, {'app.Student': 1})
# >>>

# success 
















# from django.db import models
# from django.db.models.signals import pre_save, post_save 

# # Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name

# def post_student_save(sender, instance, **kwargs):
#     print("your post has been saved")


# pre_save.connect(post_student_save, Student)           # added 
# post_save.connect(post_student_save, Student)


# # shell example 

# # >>> from app.models import Student 
# # >>> p3=Student.objects.create(name='moni')
# # your post has been saved
# # your post has been saved

# # success 













# from django.db import models
# from django.db.models.signals import pre_save, post_save 

# # Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name

# def post_student_save(sender, instance, **kwargs):
#     print("your post has been saved")

# post_save.connect(post_student_save, Student)


# # lets go into the shell land test if we get the print 

# # (virtual) PS C:\chets-django-signals\django_signals> python manage.py shell         
# # Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
# # Type "help", "copyright", "credits" or "license" for more information.
# # (InteractiveConsole)
# # >>> from app.models import Student 
# # >>> p=Student.objects.create(name="Tony")
# # your post has been saved

# # success ' your post has been saved ' printed 

# # another shell example 

# # >>> from app.models import Student 
# # >>> p2=Student()
# # >>> p2.name='chet'
# # >>> p2.save()
# # your post has been saved

# # success 