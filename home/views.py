from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, request
from django.contrib import messages
from .models import Contact
from .models import Detail
from .models import College_Info
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CreateUserForm
from .filters import DetailFilter

import sys
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser
import bs4
# Create your views here.

@login_required(login_url="login")
def index(request):
    return render(request,"base.html")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + user)
                return redirect('login')

        context ={'form':form }
        return render(request, 'register.html' ,context)
        
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Username or password may be incorrect')
                return render(request, 'login.html')

        context ={ }
        return render(request, 'login.html' ,context)


def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url="login")
def services(request):
    return render(request,"services.html")


@login_required(login_url="login")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')      
        contact = Contact(name=name, phone=phone, email=email, desc=desc)
        contact.save()
        messages.success(request, 'Your response has been submitted.')
    return render(request,'contact.html')


@login_required(login_url="login")
def bot(request):
    query = request.GET.get('query')
    
    try:
            
           
        client = wolframalpha.Client("A2EU34-QQP7VY3A8L") # Paste Your API Key Here....!!!
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'services.html', {'ans': ans})
                
                    
            
    except Exception:
        try:
                
            
            return render(request, 'services.html', {'ans': ans})
                    

        except Exception:
            try:
              
                return redirect('detail')
                

            except:
                print("It is weird but I got nothing try re-running the program")
                        


@login_required(login_url="login")
def datail_of(request):
    detail = College_Info.objects.all()
    myFilter = DetailFilter(request.GET, queryset=detail)
    detail = myFilter.qs

   
    context = {
       'myFilter':myFilter,
       'detail':detail,
    }
    return render(request, "detail.html", context)