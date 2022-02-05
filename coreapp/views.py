from django.shortcuts import render,redirect

# Create your views here.
# amal
def index(request):
    return render(request, 'TLindex.html')

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
# abin
def TLattendance(request):
    return render(request, 'TLattendance.html')

def TLreportissues(request):
    return render(request, 'TLreportissues.html')

def TLreportedissue1(request):
    return render(request, 'TLreportedissue1.html')

def TLreportedissue2(request):
    return render(request, 'TLreportedissue2.html')

def TLreport1(request):
    return render(request, 'TLreport1.html')

def TLreportsuccess(request):
    return render(request, 'TLreportsuccess.html')

# bibin
def TLtasks(request):
    return render(request, 'TLtasks.html')

def TLleave(request):
    return render(request, 'TLleave.html')

def TLleavereq(request):
    return render(request, 'TLleavereq.html')

def TLreqedleave(request):
    return render(request, 'TLreqedleave.html')

def TLgivetask(request):
    return render(request, 'TLgivetasks.html')

def TLgavetask(request):
    return render(request, 'TLgavetask.html')
    
def TLsuccess(request):
    return render(request, 'TLsuccess.html')
