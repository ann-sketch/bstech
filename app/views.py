from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import Account
import hashlib, datetime
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from .serializers import AccountSerializer
import requests

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    http_method_names = ['get']


# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def safoa_view(request):
    return render(request, 'tools/safoa.html')

def condom_view(request):
    return render(request, 'tools/condom.html')

def eye_view(request):
    if request.method=='GET':
        response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=c647dce634e344dd98f04275c22d71bd&ip_address=102.176.94.71")
        ip=response.json()['ip_address']
        city=response.json()['city']
        country=response.json()['country']
        continent=response.json()['continent']
        isVPN=response.json()['security']['is_vpn']
        carrier=response.json()['connection']['autonomous_system_organization']
        connection_type=response.json()['connection']['connection_type']
        context = {'ip':ip, 'city':city, 'country':country, 'continent': continent, 'isVPN':isVPN, 'carrier':carrier, 'connection_type': connection_type}
    return render(request, 'tools/eye.html', context)


def signup_view(request):
    signed_up=False
    if request.method == "POST":
        email = request.POST['email']
        number = request.POST['number']
        password = make_password(request.POST['password'])
        confirm_password = request.POST['confirmPassword']
        if check_password(confirm_password,password):
            try:
                Account.objects.get(email=email)
            except:
                product_key = hashlib.sha1(str.encode(str(datetime.datetime.now()))).hexdigest()
                Account.objects.create(email=email,number=number, password=password, product_key=product_key).save()
                signed_up=True
                msg = "SIGNUP SUCCESSFUL\nPRODUCT KEY => "+product_key
                return render(request,'register.html', context={"signed_up": signed_up, "msg": msg})
            else: 
                email_exists = True
                msg = "EMAIL ALREADY EXISTS"
                return render(request,'register.html', context={"email_exists": email_exists, "msg": msg})
    return render(request, 'register.html')

