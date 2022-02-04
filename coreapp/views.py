from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tldashboard(request):
    return render(request, 'TLdashboard.html')

def tlprojects(request):
    return render(request, 'TLprojects.html')

def tlprojecttasks(request):
    return render(request, 'TLprojecttasks.html')

def tlsplittask(request):
    return render(request, 'TLsplittask.html')

def tlgivetask(request):
    return render(request, 'TLgivetask.html')

def tltaskstatus(request):
    return render(request, 'TLtaskstatus.html')