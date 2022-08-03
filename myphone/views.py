from email import message
import email
from django.shortcuts import redirect, render
from .models import *


# Create your views here.


def login(request):
    error=''
    message = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)

        try:
            # exist = Customer.objects.filter(email=email, password=password).exists()
            data = Customer.objects.get(email=email, password=password)
            request.session['customer_id'] = data.id
            return redirect("home")
        except:
            print('somthing')
            message = "username or password incorrect"

    return render(request, "loginpage.html", {'errmsg': message})


def home(request):

    try:
        if request.session['customer_id']:
            return render(request, "homepage.html")
    except:
        return render(request, "loginpage.html")


    


def sign(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone_no = request.POST['phone']
        password = request.POST['password1']

        obj = Customer(first_name=first_name, last_name=last_name,
                       email=email, phone_number=phone_no, password=password)
        obj.save()
    return render(request, "signup.html")


def details(request):
    return render(request, "details.html")


def cart(request):
    return render(request, "cart.html")


def profile(request):
    # if request.method == 'POST':
    #     first_name = request.POST['firstname']
    #     last_name = request.POST['lastname']
    #     email = request.POST['email']
    #     user_name = request.POST['username']
    #     country = request.POST['country']

    #     obj = Cust_profile(first_name=first_name,last_name=last_name,
    #     email=email,user_name=user_name,country=country)
    #     obj.save()

    return render(request, "profile.html")


def dtls1(request):
    return render(request, "dtls1.html")


def dtls2(request):
    return render(request, "dtls2.html")


def dtls3(request):
    return render(request, "dtls3.html")

def logout(request):
    del request.session['customer_id']
    print("hello")
    return render(request,"loginpage.html")
