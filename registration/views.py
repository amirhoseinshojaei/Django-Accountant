from django.shortcuts import render,HttpResponse
import random,string
import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.crypto import get_random_string
from datetime import datetime
from django.contrib.auth.hashers import make_password
from .models import PasswordresetCodes
from accountant.models import Token
# Create your views here.
# create random string for token
random_str = lambda N: ''.join(
    random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def grecaptcha_verify(request):
    if request.method == 'POST':
        response = {}
        data = request.POST
        captcha_rs = data.get('g-recaptcha-response')
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': captcha_rs,
            'remoteip': get_client_ip(request)
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        response["status"] = verify_rs.get("success", False)
        response['message'] = verify_rs.get('error-codes', None) or "Unspecified error."
        return HttpResponse(response)

def register(request):
    if request.POST.has_key(
        'requestcode'
    ): # form is filled. if not spam, generate code and save in db, wait for email confirmation, return message
        
        if not grecaptcha_verify(request):
            context={
                'message':'captcha was not correct'
            }
            return render (request,'register.html',context)
        
        # duplicate email
        if User.objects.filter(email=request.POST['email']).exists():
            context = {
                'message':'this email is exist'
            }
            return render (request,'register.html',context)
        
        # if user does not exist
        if not User.objects.filter(request.POST['username']).exists():
            code = get_random_string(length=32)
            now = datetime.now()
            email = request.POST['email']
            password = make_password(request.POST['password'])
            username = request.POST['username']
            temporarycode = PasswordresetCodes(
                code = code , email = email , time = now , username = username , password = password
            )
            temporarycode.save()

            # message send

            message = 'send email for activate account'
            message = " Happy , i am amirhosein shojaei,happy developer "
            body = "this linke for activate account:  <a href=\"{}?code={}\">Click here</a>".format(request.build_absolute_url('/accounts/register/'), code)
            message = message + body
            context = {
                'message':message
            }
            return render (request,'index.html',context)
        else:
            context = {
                'message':"  the username is already used   "
            }
            return render (request,'register.html',context)
        #  user clicked on code
    elif request.GET.has_key('code'):
        code = request.GET['code']
        if PasswordresetCodes.objects.filter(
            code=code
        ).exists(): # if code is in temporary db, read the data and create the user
            new_temp_user = PasswordresetCodes.objects.get(code=code)
            new_user = User.objects.create(
                username = new_temp_user.username,
                password = new_temp_user.password,
                email = new_temp_user.email
            )
            this_token = get_random_string(length=48)
            token = Token.objects.create(user = new_user , token = this_token)
            # delet the temporary activation code from db
            PasswordresetCodes.objects.filter(code=code).delete()
            context = {
                'message':"your account is created, your token is{},please save this token because it is no longer display".format(
                    this_token
                )
            }
            return render (request,"index.html",context)
        else:
            context = {
                'message':"the activation link is not valid,try again"
            }
            return render (request,'register.html',context)
        
    else:
        context = {'message':''}
        return render (request, 'register.html',context)