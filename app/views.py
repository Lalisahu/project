from django.shortcuts import render,redirect
from .models import Student

def home(request):
    return render(request, 'home.html')  


def about(request):
    return render(request, 'about.html') 
def contact(request):
    return render(request, 'contact.html')  
def base(request):
    return render(request, 'base.html')  
def registen(request):
    return render(request, 'registen.html')  
    
    
def registen_form(request):
    print("registen_form")
    print(request.POST)
    print(request.method)
    print(request.FILES)
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    print(username,password,email,first_name,last_name,phone,dob)
    Student.objects.create(student_name=username,student_email=email,student_phone=phone,student_dob=dob)






# Create your views here.
