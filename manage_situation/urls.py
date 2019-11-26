
from django.urls import path, include
from django.conf.urls.static import static
import manage_situation.views
urlpatterns = [
    path('createcategory/',manage_situation.views.createcategory, name='createcategory'),
    path('createstudentid/',manage_situation.views.createstudentid, name='createstudentid'),
    path('managecenter/',manage_situation.views.managecenter, name='managecenter'),
    
] 
