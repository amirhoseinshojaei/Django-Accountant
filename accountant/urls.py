from .import views
from django.urls import path
# #######
urlpatterns=[
    path ('submit/expense/',views.submit_expense, name= 'sumbit_expense'),
    path ("submit/income/",views.submit_income, name= 'submit_income'),
    path ("query/generalstat/",views.generalstat, name= 'generalstat'),
    path ('query/incomestat/',views.income_stat, name = 'incomestat'),
    path ('query/expensestat/', views.expense_stat , name = 'expensestat'),
    path ('query/incomes/', views.query_income, name = 'query_incomes'),
    path ('query/expenses/', views.query_expense, name = 'query_expenses'),
    path ('',views.index, name= 'index'),
]