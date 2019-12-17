
from django.urls import path, include
from django.conf.urls.static import static
import status.views
urlpatterns = [
    path('createcategory/',status.views.createcategory, name='createcategory'),
    path('createstudentid/',status.views.createstudentid, name='createstudentid'),
    path('managecenter/',status.views.managecenter, name='managecenter'),
    
] 
