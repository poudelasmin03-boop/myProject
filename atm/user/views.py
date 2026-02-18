from django.shortcuts import render
from .models import open_account
# Create your views here.



def atm_views(request):
  return render(request,'atm.html')


def open_account_views(request):
  if request.method=='POST':
    firstname=request.POST.get('firstname')
    middlename=request.POST.get('middlename')
    lastname=request.POST.get('lastname')
    age=request.POST.get('age')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    province=request.POST.get('province')
    city=request.POST.get('city') 
    address=request.POST.get('address')
    
 
   

    
   
    if len(phone)!=10:
      return render(request,'openacc.html',{'error':'Phone have exactly 10 character',
      'firstname':firstname,
      'middlename':middlename,
      'lastname':lastname,
      'age':age,
      'phone':phone,
      'email':email,
      'province':province,
      'city':city,
      'address':address})
    
    
    
    account=open_account.objects.create(firstname=firstname,
                                middlename=middlename,
                                lastname=lastname,
                                age=age,
                                phone=phone,
                                email=email,
                                province=province,
                                city=city,
                                address=address )  
    

    
    
    return render(request,'home.html',{'success':f'{firstname} {middlename} {lastname}   your account has been  created and account nbr is {account.account_nbr}'})  # it's means account number stored on DB
  
  return render(request,'openacc.html',{'page':'open'})

def deposite(request):
  if request.method=='POST':
    account_nbr=request.POST.get('account_nbr').strip()
    amount=request.POST.get('amount')
    
    
    amount=float(amount)
    Account=open_account.objects.filter(account_nbr=account_nbr).first()  #Noted exists return true and false ==>Boolean  
                                                                          #Firsts  returb objects value or none  ==>Model objectt
    
    if  Account is None:
     return render(request,'deposite.html',{'error':'Please Enter a valid Account Number',
                                         'account_nbr':account_nbr,
                                         'amount':amount})
       
    Account.balance += amount
    Account.transcation='deposite'
    Account.save()
  
    return render(request,'home.html',{'loadsuccess':f'{amount} is loaded sucessfully in your Account'})
    
  return render(request,'deposite.html')
    
    
def transfer(request):
  
  if request.method=='POST':
    sender_nbr=request.POST.get('sender')
    receiver_nbr=request.POST.get('receiver')
    amount=(request.POST.get('amount'))
   
    if sender_nbr==receiver_nbr:
      return render(request,'transfer.html',{'error':'Please Enter a valid Account Number',
                                         'sender':sender_nbr,
                                         'receiver':receiver_nbr,
                                         'amount':amount})
   
  
  
    sender=open_account.objects.filter(account_nbr=sender_nbr).first()
    receiver=open_account.objects.filter(account_nbr=receiver_nbr).first()
    
   
    amount=float(amount)
    if sender.balance<amount:
      return render(request,'transfer.html',{'error':'Insufficent balance..',
                                            'sender':sender_nbr,
                                         'receiver':receiver_nbr,
                                         'amount':amount})    
    
    if  sender is None or  receiver is None:
          return render(request,'transfer.html',{'error':'Invalid sender or reciver account number',
                                            'sender':sender_nbr,
                                         'receiver':receiver_nbr,
                                         'amount':amount})    
   
    sender.balance-=amount
    receiver.balance+=amount
    sender.transcation='transfer'
    receiver.transcation='tranfer'
    sender.save()
    receiver.save()
  
    return render(request,'home.html',{'success':f'{amount} is transfered  to {receiver_nbr}'})
        
  return render(request,'transfer.html',{'page':'transfer'})
 
def check_balance(request):
  if request.method=='POST':
    firstname=request.POST.get('firstname')
    account_nbr=request.POST.get('account_nbr')
    
    
    Account=open_account.objects.filter(firstname=firstname,account_nbr=account_nbr).first()
    
    if not Account :
      return render(request,'check.html',{'error':'Username  or Account number doesnot exits','firstname':firstname,
      'account_nbr':account_nbr})
    
    
    return render(request,'home.html',{'success':f'{firstname} has {Account.balance}'})      
    
    
    
  return render(request,'check.html')
    
    
    
def home(request):
   return render(request,'home.html',{'page':'home'})
 
 
    

def statements_viwes(request):


  users=open_account.objects.filter(transcation='deposit')
  return render(request,'transction.html',{'users':users} )  
