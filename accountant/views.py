from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.contrib.auth.models import User
from datetime import datetime
from .models import (Expense,Income)
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Aggregate , Count , Sum
from django.contrib.auth.hashers import check_password
from django.core import serializers
# Create your views here.

@csrf_exempt
def submit_expense(request):
    """submit an expense"""

    if request.method=='POST':
        this_token = request.POST.get('token')

        try:
            this_user= User.objects.get(token__token=this_token)
        
        except User.DoesNotExist:

            return JsonResponse({'error':'invalid_token'},status=400)
        
        this_bought= request.POST.get('bought')

        this_amount = request.POST.get('amount')

        if 'date' in request.POST:
            this_date = request.POST['date']
        else:
            this_date = datetime.now()

        Expense.objects.create(
            user = this_user,
            bought = this_bought,
            amount = this_amount,
            date = this_date
        )

        return JsonResponse({
            'success':'Expense submitted successfull',
        },status=200)
    else:
        return JsonResponse({
            'error':'Invalid request method',
        }, status=400)

@csrf_exempt
def submit_income(request):
    """submit an income"""
    if request.method=="POST":
        this_token = request.POST.get('token')

        try:
            this_user = User.objects.get(token__token=this_token)
        
        except User.DoesNotExist:

            return JsonResponse({
                'error':'Invaldid user',
            }, status=400)
        
        if 'date' not in request.POST:
            this_date = datetime.now

        else:
            this_date= request.POST['date']
        
        this_text= request.POST.get('text')
        
        this_amount = request.POST.get('amount')

        Income.objects.create(
            
            user = this_user,
            date = this_date,
            amount = this_amount,
            text = this_text
        )
        return JsonResponse({
            'success':"Income submitted successfull",
        }, status=200)
    else:
        return JsonResponse({
            'error':'Invalid request',
        }, status = 400)
    
def index(request):
    context ={}
    return render (request,'index.html',context)

@csrf_exempt

def generalstat(request):
    # TODO: should get a valid duration
    # TODO: is the token valid ?
    
    if request.method=='POST':
        this_token = request.POST.get('token')
        try:
            this_user = User.objects.get(token__token= this_token)
        except User.DoesNotExist:

            return JsonResponse({
                'error': 'invalid user'
            }, status = 400)
        income = Income.objects.filter(user = this_user).aggregate(count=Count('amount'),total= Sum('amount'))
        expense = Expense.objects.filter(user = this_user).aggregate(count=Count('amount'),total= Sum('amount'))
        context={}
        context['expense'] = expense
        context['income'] = income

        return JsonResponse (context, encoder= JSONEncoder)
    else:
        return JsonResponse({
            'error':'invalid request'
        }, status = 400)
    
def income_stat(request):
    if request.POST.__contains__('username') and  request.POST.__contains__('password'):
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        try:
            this_user = User.objects.get(username = username)
        except User.DoesNotExist:
            context:{}
            context['error'] = 'invalid user'
            return JsonResponse (
                context,
                encoder= JSONEncoder
            )
        if (check_password(password, this_user.password)):
            income = Income.objects.get(user = this_user)
            context:{}
            context["income"] = income
            return JsonResponse(context , encoder= JSONEncoder)
        else:
            return JsonResponse ({
                'error': "your password is wrong"
            }, status = 400)
        
    else:
        return JsonResponse({
            "error": 'your request method is not safe'
        }, status = 400)
    

def expense_stat(request):
    if request.POST.__contains__('username') and request.POST.__contains__('password'):
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        try:
            this_user = User.objects.get (username = username)
        except User.DoesNotExist:
            return JsonResponse({
                'error':'invalid '
            }, status = 400)
        if (check_password('password'), this_user.password):
            this_expense = Expense.objects.get(user = this_user)
            expense = this_expense.amount
            context={}
            context['amount'] = expense
            return JsonResponse(context , encoder= JSONEncoder)
        else :
            return JsonResponse({
                'error': 'your username is wrong'
            }, status = 400)
    else:
        return JsonResponse({
            'error': 'invalid request method'
        }, status = 400)
    

@csrf_exempt    
def query_income (request):
    
    if request.method == 'POST':
        this_token = request.POST.get('token')
        num = request.POST.get('count',11)
        try:
            this_user = User.objects.get(token__token = this_token)
        except User.DoesNotExist:
            return JsonResponse ({
                'error': 'invalid user'
            }, status = 400)
        incomes = Income.objects.filter(user = this_user).order_by('-date')[:num]
        incomes_serialized = serializers.serialize ("json",incomes)
        return JsonResponse (incomes_serialized , encoder= JSONEncoder, safe= False)

    


