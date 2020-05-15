from django.shortcuts import render

# Create your views here.

def list(request):
    #list will be imported from a Model here
    return render(request,'area/list.html')
