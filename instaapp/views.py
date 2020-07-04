from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .email import send_signup_email
from .forms import NewProfileForm

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


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account_holder = current_user
            profile.save()
        return redirect('my-profile')

    else:
        form = NewProfileForm()
    return render(request, 'create_profile.html', {"form": form})
