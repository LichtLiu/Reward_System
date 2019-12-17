from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Student_id, Manage_Center

def home(request):
    return render(request,'status/home.html')

def managerhome(request):
    situation_list = Manage_Center.objects.all()
    context = {
        'situations':situation_list
    }
    return render(request,'status/managerhome.html', context)
# Create your views here.
@login_required
def createcategory(request):
    if request.method == 'POST':
        if request.POST['category']  and request.POST['time'] and request.POST['point']:
            cat = Category()
            cat.category = request.POST['category']
            cat.cause =  request.POST.get('cause',False)
            cat.time = request.POST['time']
            cat.point = request.POST['point']
            cat.manager = request.user
            cat.save()
            return redirect('managerhome')

        else:
            return render(request,'status/createcategory.html',{'error':'nope'})

    else:
        return render(request,'status/createcategory.html')



@login_required
def createstudentid(request):
    if request.method == 'POST':
        if request.POST['id'] and request.POST['number'] and request.POST['name']:
            student = Student_id()
            student.id = request.POST['id']
            student.number = request.POST['number']
            student.name = request.POST['name']
            student.manager = request.user
            student.save()
            return redirect('managerhome')

        else:
            return render(request,'status/createstudentid.html',{'error':'nope'})

    else:
        return render(request,'status/createstudentid.html')

def managecenter(request):
    studentdata = Student_id.objects
    categorydata = Category.objects
    cause = Category.objects.filter(category="加點")
    if request.method == 'POST':
        if request.POST['student_id'] and request.POST['category'] and request.POST['cuase'] and request.POST['pub_date'] and request.POST['manager']:
            manage = Manage_Center()
            manage.student_id = request.POST['student_id']
            manage.category = request.POST['category']
            manage.cuase = request.POST['cuase']
            manage.pub_date = request.POST['pub_date']
            manage.manager = request.user
            return redirect('managerhome')
        else:
            return render(request,'status/managesituation.html',{'error':'nope'})
    else:
        return render(request,'status/managesituation.html',{"student":studentdata,"category":categorydata,"cause":cause})
