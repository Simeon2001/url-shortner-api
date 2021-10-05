from django.shortcuts import redirect, render
from .models import links
from django.http import HttpResponseRedirect

# Create your views here.
def rework (request,hash):
    p = hash
    link = links.objects.get(extension=p)
    print (link.url)
    return HttpResponseRedirect(link.url)