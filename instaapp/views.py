from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .email import send_signup_email

# Create your views here.
def welcome(request):      
    
    return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def home(request):

    return render(request, 'home-page.html')
    

@login_required(login_url='/accounts/login/')
def send_email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email(name, email)
    return HttpResponseRedirect('/')
