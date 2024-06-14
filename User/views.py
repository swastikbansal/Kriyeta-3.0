from django.shortcuts import render

# Create your views here.
def dahsboard(request): 
    return render(request,'index.html')