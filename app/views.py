from django.shortcuts import render,redirect

def home(request):
    return render(request, 'home.html')  # Render the home.html template


def about(request):
    return render(request, 'about.html')  # Render the about.html template
def contact(request):
    return render(request, 'contact.html')  # Render the contact.html template
def base(request):
    return render(request, 'base.html')  # Render the base.html template
def registen(request):
    return render(request, 'registen.html')  # Render the register.html template
    
    
def registen_form(request):
    print("registen_form")
    print(request.POST)
    print(request.method)
    print(request.Files)
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    dob = request.POST.get('dob')
    print(username,password,email,first_name,last_name,phone,address,dob)







# Create your views here.
