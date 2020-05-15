from django.shortcuts import render
from .models import Area
# Create your views here.

def list(request):
    areas = Area.objects.all()
    return render(request,'area/list.html',{'areas':areas})
