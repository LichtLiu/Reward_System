from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Student, Manage_Center
from datetime import datetime, timedelta
def home(request):
    one_week_ago = datetime.today() - timedelta(days=7)
    filter_by_week = Manage_Center.objects.filter(pub_date__gte=one_week_ago)
    context = {
        'filter_by_week':filter_by_week
    }
    return render(request,'status/home.html',context)

def managerhome(request):
    situation_list = Manage_Center.objects.all()
    one_week_ago = datetime.today() - timedelta(days=7)
    filter_by_week = Manage_Center.objects.filter(pub_date__gte=one_week_ago)
    context = {
        'situations':situation_list,
        'filter_by_week':filter_by_week
    }
    return render(request,'status/managerhome.html', context)


@login_required
def createcategory(request):
    if request.method == 'POST':
        if request.POST['category']  and request.POST['time'] and request.POST['point']:
            cat = Category()
            cat.category = request.POST['category']
            cat.cause =  request.POST.get('cause')
            cat.time = request.POST['time']
            cat.point = request.POST['point']
            cat.manager = request.user
            cat.save()
            return redirect('managerhome')

        else:
            return render(request,'status/createcategory.html',{'error':'nope'})

    else:
        return render(request,'status/createcategory.html')

def categoryview(request):
    category = Category.objects.all()
    return render(request,'status/categoryview.html',{'category':category})

def deletecat(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("categoryview")
        


@login_required
def createstudentid(request):
    if request.method == 'POST':
        if request.POST['number'] and request.POST['name']:
            student = Student()
            student.student_id = request.POST['student_id']
            student.number = request.POST['number']
            student.name = request.POST['name']
            student.manager = request.user
            student.save()
            return redirect('managerhome')

        else:
            return render(request,'status/createstudentid.html',{'error':'nope'})

    else:
        return render(request,'status/createstudentid.html')

def studentview(request):
    student = Student.objects.order_by('number')
    return render(request,'status/studentview.html',{'student':student})

def deletestudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("studentview")
# def managecenter(request):
#     studentdata = Student.objects
#     category = Category.objects
#     if request.method == 'POST':
#         if request.POST['student_id'] and request.POST['category'] and request.POST['pub_date']:
#             manage = Manage_Center()
#             student_id = request.POST['student_id']
#             manage.category = request.POST['category']
#             manage.pub_date = request.POST['pub_date']
#             manage.manager = request.user
#             manage.save()
#             return redirect('managerhome')
#         else:
#             return render(request,'status/managesituation.html',{'error':'nope'})
#     else:
#         return render(request,'status/managesituation.html',{"student":studentdata,"category":category })

def managecenter(request):
    studentdata = Student.objects.get(student_id="1100630224")
    Student.objects.filter(id=studentdata.id)
    category = Category.objects.get(category="加點")
    Category.objects.filter(id=category.id)
    if request.method == 'POST':
        if request.POST['pub_date']:
            manage = Manage_Center()
            manage.student_id = studentdata
            manage.category = category
            manage.pub_date = request.POST['pub_date']
            manage.manager = request.user
            manage.save()
            return redirect('managerhome')
        else:
            return render(request,'status/managesituation.html',{'error':'nope'})
    else:
        return render(request,'status/managesituation.html',{"student":studentdata,"category":category })