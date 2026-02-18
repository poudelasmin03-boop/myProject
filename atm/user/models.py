from django.db import models
import random
from django.utils import timezone
# Create your models here.
def account_number():
  return str(random.randint(1000000000,9999999999))


 
  #openAccount
  
class open_account(models.Model):
  Transcation_Choices=(('depsoite','Deposite'),('transfer','Transfer'))
  transcation=models.CharField(max_length=100,choices=Transcation_Choices)
  account_nbr=models.CharField(max_length=10,unique=True,default=account_number,editable=False)
  firstname=models.CharField(max_length=100)
  middlename=models.CharField(max_length=100)
  lastname=models.CharField(max_length=100,default='abc',null=False)
  age=models.PositiveIntegerField()
  phone=models.CharField(max_length=10)
  email=models.EmailField(null=False,default='example123@gmail.com')
  province=models.CharField(max_length=40,default='Lumbini')
  city=models.CharField(max_length=100,default='kohalpur')
  address=models.CharField(max_length=100)
  balance=models.FloatField(default=0)
  date=models.DateTimeField(default=timezone.now(),null=False)


  def __str__(self):
    return self.firstname
  
  