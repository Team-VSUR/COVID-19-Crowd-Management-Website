from django.shortcuts import render
from .models import Ticket
from . import forms

# Create your views here.
def ticket_generation(request):
    if request.method == "POST":
        form = forms.CreateTicket(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
        return redirect("home")
    else:
        form = forms.CreateTicket
        return render(request,'tickets/ticket_generation.html',{'form':form})
