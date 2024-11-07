from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about (request):
    return render(request,'About.html')
def contact (request):
    return render(request, 'Contact.html')
def blog (request):
    return render(request, 'blog.html')
def services (request):
    return render(request, 'Services.html')
def portfolio(request):
    return render(request,'portfolio.html')
def testimonies(request):
    return render(request,'testimonies.html')


