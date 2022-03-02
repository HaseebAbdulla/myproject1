from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"loginpage.html")

def home(request):
    return render(request,"homepage.html")


def sign(request):
    return render(request,"signup.html")    

def details(request):
    return render(request,"details.html")

def cart(request):
    return render(request,"cart.html")

def profile(request):
    return render(request,"profile.html")





