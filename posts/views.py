from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Post
# Create your views here.


# request_counter_signal = Signal(providing_args=['timestamp'])       # getting error no providing_args 
request_counter_signal = Signal('timestamp')

def post_view(request):
    request_counter_signal.send(sender=Post, timestamp='2022-6-1')
    return HttpResponse("post view signals with JustDjango")

@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print('post request finshed with JustDjango')

@receiver(request_counter_signal)
def post_counter_signal(sender, **kwargs):
    # print('post counter finshed with JustDjango')
    print(kwargs)


















# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.signals import request_finished
# from django.dispatch import receiver
# # Create your views here.

# def post_view(request):
#     return HttpResponse("post view signals with JustDjango")

# @receiver(request_finished)
# def post_request_receiver(sender, **kwargs):
#     print('request finshed with JustDjango')



# # when we run localhost7000/posts/posts and localhost7000 will get print string which is basically request is finshed 