
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import manage_situation.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',manage_situation.views.home, name='home'),
    path('manager_home/',manage_situation.views.managerhome, name='managerhome'),
    path('account/',include('account.urls')),
    path('manage_situation/',include('manage_situation.urls')),
    
]
