from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include

urlpatterns=[
    path('',views.ticket_generation,name='ticket_generation')
]
