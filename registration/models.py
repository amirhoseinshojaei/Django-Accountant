from django.db import models

# Create your models here.
class PasswordresetCodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.EmailField()
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
