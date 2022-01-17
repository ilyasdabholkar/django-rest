from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from api.views import getMembers

def index(request):
    return redirect(getMembers)
