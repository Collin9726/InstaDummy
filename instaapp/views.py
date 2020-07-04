from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .email import send_signup_email
from .forms import NewProfileForm, NewImageForm
from .models import Profile, Image, Comment

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
    return redirect(create_profile)


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account_holder = current_user
            profile.save()
        return redirect(my_profile)

    else:
        form = NewProfileForm()
    return render(request, 'create-profile.html', {"form": form})



@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    images = Image.objects.filter(profile = profile).order_by('-posted')    

    return render(request, 'my-profile.html', {"profile": profile, "images": images})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            this_image = form.save(commit=False)
            this_image.profile = profile
            this_image.save()
        return redirect(my_profile)

    else:
        form = NewImageForm()
    return render(request, 'upload-image.html', {"form": form})


@login_required(login_url='/accounts/login/')
def delete_image(request, image_id):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()   

    if image.profile == profile:
        image.delete_image()
        return redirect(my_profile)
    else:
        raise Http404()


@login_required(login_url='/accounts/login/')
def update_caption(request, image_id):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()

    if image.profile == profile:
        if 'newcaption' in request.GET and request.GET["newcaption"]:
            new_caption = request.GET.get("newcaption")
            image.caption = new_caption
            image.update_caption()
            return redirect(my_profile)
        else:
            return render(request, 'update-caption.html', {"image":image})

    else:
        raise Http404()



