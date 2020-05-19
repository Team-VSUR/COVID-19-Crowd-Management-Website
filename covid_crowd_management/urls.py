from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('emergency',views.emergency,name='emergency'),
    path('area/',include('area.urls')),
    path('accounts/',include('accounts.urls')),
    path('tickets/',include('tickets.urls')),
]
