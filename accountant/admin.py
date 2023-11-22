from django.contrib import admin
from .models import Expense,Income,Token
# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'bought',
        'date',
        'user',
        'amount'
    ]
    list_filter = ['date']
    search_fields = ['date','user']
    ordering = ['date']
admin.site.register(Expense,ExpenseAdmin)

class IncomAdmin(admin.ModelAdmin):
    list_display = [
        'text',
        'date',
        'user',
        'amount'
    ]
    list_filter = ['date']
    search_fields = ['text','user','amount']
    ordering = ['date']

admin.site.register(Income,IncomAdmin)

class TokenAdmin(admin.ModelAdmin):
    list_display =[
        'user',
        'token'
    ]
    search_fields = ['user']

admin.site.register(Token,TokenAdmin)