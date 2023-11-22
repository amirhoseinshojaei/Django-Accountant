from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.contrib.auth.models import User
from datetime import datetime
from .models import (Expense,Income)
from django.views.decorators.csrf import csrf_exempt
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


