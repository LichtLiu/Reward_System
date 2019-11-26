
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import reward.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',reward.views.home, name='home'),
    path('account/',include('account.urls')),
    
]
