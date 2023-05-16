
from django.shortcuts import render,redirect
from .models import journels,userdetails
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def index(request):
    
    context = {'title': 'Portfolio',}
    return render(request, '1dis.html', context)

class registerview(CreateView):
    models = userdetails
    fields =['name','mobile','email','password','confirm']
    template_name = "journel/register.html"
    success_url =reverse_lazy('userlogin')
    def get_queryset(self):
        return userdetails.objects.none()

def login_view(request):
    if request.method == 'POST':

        
        email=request.POST["email"]
        password=request.POST["password"]
        user = userdetails.object.filter(email=email,password=password).first()
        
        if user is not none:
            user = authenticate(request,email=email,password=password)
            login(request,user)
            return redirect('createjournel')
    return render(request,'journel/login.html')


class JournelCreateView(CreateView):


    model = journels
    fields =['Products','amount','Invoice','Date']
    template_name = "journel/create.html"
    success_url =reverse_lazy('listjournel')


class JournelListView(ListView):
      model = journels
      template_name = "journel/list.html"
      