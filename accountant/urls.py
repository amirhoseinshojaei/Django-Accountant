from .import views
from django.urls import path
# #######
urlpatterns=[
    path ('submit/expense/',views.submit_expense, name= 'sumbit_expense'),
    path ("submit/income/",views.submit_income, name= 'submit_income'),
    path ("query/generalstat/",views.generalstat, name= 'generalstat'),
    path ('',views.index, name= 'index'),
]