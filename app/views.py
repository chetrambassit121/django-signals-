from django.shortcuts import render, HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver


def index(request):
    return HttpResponse("<h1>Welcome to Chets Django Signals Basic</h1>")


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
