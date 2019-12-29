
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import status.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',status.views.home, name='home'),
    path('manager_home/',status.views.managerhome, name='managerhome'),
    path('account/',include('account.urls')),
    path('situation/',include('status.urls')),
    path('deletecat/<int:id>',status.views.deletecat, name='deletecat'),
    path('deletestudent/<int:id>',status.views.deletestudent, name='deletestudent'),
]
