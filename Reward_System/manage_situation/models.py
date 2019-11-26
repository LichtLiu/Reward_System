from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=20)
    cuase = models.CharField(max_length=50)
    time = models.PositiveIntegerField(default=0)
    point = models.PositiveIntegerField(default=0)
    manager = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.category

class Student_id(models.Model):
    id =  models.PositiveIntegerField(primary_key=True)
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    manager = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.number)
    
# Create your models here.
class Manage_Center(models.Model):
    student_id = models.ForeignKey(Student_id,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    cuase = models.CharField(max_length=50)
    time = models.PositiveIntegerField(default=0)
    point = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField()
    manager = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_id)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')



