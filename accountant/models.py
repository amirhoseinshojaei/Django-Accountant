from django.db import models
from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
    token = models.CharField( max_length= 30, default= get_random_string (length= 30))
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return "{}-{}".format(self.token,self.user)
    

class Expense(models.Model):
    bought = models.CharField(max_length= 255)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.BigIntegerField()

    def __str__(self):
        return "{}-{}".format(self.date,self.bought)
    
class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.date,self.text)
    
class New(models.Model):
    title = models.CharField (max_length = 255)
    description = models.TextField (max_length = 1500)
    date = models.DateTimeField (auto_now=False,auto_now_add=True)
    user = models.ForeignKey (User , on_delete = models.CASCADE)