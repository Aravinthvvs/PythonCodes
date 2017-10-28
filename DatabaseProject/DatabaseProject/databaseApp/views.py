from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def getStudentAge(request):
    student = Student.objects.get(pk=3)
    age = student.getAge()
    name = student.getName()
    context = {'name':name,'age':age}
    return render(request,'databaseApp/students.html',context)
