from django.shortcuts import render, HttpResponse

def index(request):

 return render(request, 'index.html')

def about(request):
 return render(request,'aboutus.html')

def services(request):
 return render(request, 'services.html')

def contactus(request):
 return render(request, 'contactus.html')
