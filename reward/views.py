from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'reward/home.html')
# Create your views here.
@login_required
def create_category(request):
    return render(request, 'reward/create_category.html')