from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'portfolio/home.html')

def about(request):
    return render(request,'portfolio/about.html')

def contact(request):
    return render(request,'portfolio/contact.html')

def projects(request):
    return render(request, 'portfolio/projects.html')
