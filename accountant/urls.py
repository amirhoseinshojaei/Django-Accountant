from .import views
from django.urls import path
# #######
urlpatterns=[
    path ('submit/expense/',views.submit_expense, name= 'sumbit_expense'),
    path ("submit/income/",views.submit_income, name= 'submit_income'),
    path ("query/generalstat/",views.generalstat, name= 'generalstat'),
    path ('incomestat/',views.income_stat, name = 'incomestat'),
    path ('expensestat/', views.expense_stat , name = 'expensestat'),
    path ('query/incomes/', views.query_income, name = 'query_incomes'),
    path ('',views.index, name= 'index'),
]