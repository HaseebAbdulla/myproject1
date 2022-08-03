from django.shortcuts import render

# Create your views here.

def adminmaster(request):
    return render(request, "adminmaster.html")