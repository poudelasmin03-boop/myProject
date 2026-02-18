from django.shortcuts import render,redirect

# Create your views here.
def home_views(request):
  if 'count' in  request.session:
    request.session['count']+=1
  else:
       request.session['count']=1
            
  return render(request ,'index.html',{
    'count':request.session['count']
  })
  
  
def form_views(request):
  if request.method=="POST":  
    request.session['username']=request.POST.get('username')
    request.session['address']=request.POST.get('address')
    return redirect('home')
  return render(request,'form.html') 


def flush_data(request):
  request.session.flush()
  return render(request,'index.html')

    
    