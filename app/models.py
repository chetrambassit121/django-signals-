from django.db import models
from django.db.models.signals import pre_save, post_save 

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

def post_student_save(sender, instance, **kwargs):
    print("your post has been saved")

post_save.connect(post_student_save, Student) 