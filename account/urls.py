
from django.urls import path, include
from django.conf.urls.static import static
import account.views
urlpatterns = [
    path('signup/',account.views.signup, name='signup'),
    path('login/',account.views.login, name='login'),
    path('logout/',account.views.logout, name='logout'),
] 
