from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tlprofile(request):
    return render(request, 'TLprofile.html')

def tlprojects(request):
    return render(request, 'TLprojects.html')

def tlprojecttasks(request):
    return render(request, 'TLprojecttasks.html')

def tlsplittask(request):
    return render(request, 'TLsplittask.html')

def tlgivetask(request):
    return render(request, 'TLgivetask.html')