from django.shortcuts import render, HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Student

request_your_signal=Signal('time')
def index(request):
    request_your_signal.send(sender=Student, time=['one time'])
    return HttpResponse("<h1>Welcome to Chets Django Signals Basic</h1>")


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("One Request finished!")

@receiver(request_your_signal)
def my_callback1(sender, **kwargs):
    print("Custom Request finished!")

@receiver(request_your_signal)
def my_callback2(sender, **kwargs):
    print(kwargs)


# run server 

# (virtual) PS C:\chets-django-signals\django_signals> python manage.py runserver 7000
# Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced).
# May 31, 2022 - 18:54:54
# Django version 4.0.4, using settings 'SRC.settings'
# Starting development server at http://127.0.0.1:7000/
# Quit the server with CTRL-BREAK.
# Custom Request finished!
# {'signal': <django.dispatch.dispatcher.Signal object at 0x0478C6B8>, 'time': ['one time']}
# [31/May/2022 18:54:56] "GET / HTTP/1.1" 200 46
# One Request finished!












# from django.shortcuts import render, HttpResponse
# from django.core.signals import request_finished
# from django.dispatch import receiver


# def index(request):
#     return HttpResponse("<h1>Welcome to Chets Django Signals Basic</h1>")


# @receiver(request_finished)
# def my_callback(sender, **kwargs):
#     print("One Request finished!")



# # when we runserver and go to localhost will get the print ()

# # System check identified no issues (0 silenced).
# # May 31, 2022 - 18:41:41
# # Django version 4.0.4, using settings 'SRC.settings'
# # Starting development server at http://127.0.0.1:7000/
# # Quit the server with CTRL-BREAK.
# # [31/May/2022 18:41:53] "GET / HTTP/1.1" 200 46
# # One Request finished!
