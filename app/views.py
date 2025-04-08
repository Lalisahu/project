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










# Create your views here.
