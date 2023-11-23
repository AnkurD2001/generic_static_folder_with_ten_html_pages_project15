from django.shortcuts import render

# Create your views here.
def inlinestyle(request):
    return render(request,'inlinestyle.html')

def internalstyle(request):
    return render(request,'internalstyle.html')

def table(request):
    return render(request,'table.html')

def forms(request):
    return render(request,'forms.html')

def navbar(request):
    return render(request,'navbar.html')

def flexbox(request):
    return render(request,'flexbox.html')

def boxmodel(request):
    return render(request,'boxmodel.html')

def iframe(request):
    return render(request,'iframe.html')

def transforms(request):
    return render(request,'transforms.html')

def pseudoclassselector(request):
    return render(request,'pseudoclassselector.html')






