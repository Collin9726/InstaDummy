from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .email import send_signup_email
from .forms import NewProfileForm, NewImageForm, NewFollowForm, NewUnfollowForm
from .models import Profile, Image, Comment, Follow

# Create your views here.
def welcome(request):      
    
    return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user 
    pk_list=[]
    try:
        profile_mine = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    my_images = Image.objects.filter(profile = profile_mine)
    for image in my_images:
        pk_list.append(image.id)

    i_follow = Follow.objects.filter(follower = profile_mine)
    for prof in i_follow:
        their_profile = prof.followed
        their_images = Image.objects.filter(profile = their_profile)
        for image in their_images:
            pk_list.append(image.id)

    timeline_images = Image.objects.filter(pk__in = pk_list).order_by('-posted')

    return render(request, 'home-page.html', {"images": timeline_images})


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


@login_required(login_url='/accounts/login/')
def change_profile_photo(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        profile.profile_photo = request.FILES['img']        
        profile.update_profile()
        return redirect(my_profile)
    
    return render(request, 'update-prof-pic.html')


@login_required(login_url='/accounts/login/')
def delete_profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    profile.delete_profile()
    current_user.delete()
    
    return redirect(welcome)


@login_required(login_url='/accounts/login/')
def search_profile(request):
    users=User.objects.all()    

    if 'uname' in request.GET and request.GET["uname"]:
        search_term = request.GET.get("uname")        
        this_user=None
        try:
            this_user = User.objects.get(username__icontains=search_term)            
        except User.DoesNotExist:
            pass 

        profile = None
        try:
            profile = Profile.objects.get(account_holder = this_user) 
        except Profile.DoesNotExist:
            pass          
        
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "profile":profile})

    else:
        blank_message = "You haven't searched for any user."
        return render(request, 'search.html',{"blank_message":blank_message})


@login_required(login_url='/accounts/login/')
def user_profile(request, profile_id): 
    current_user = request.user   
    try:
        profile = Profile.objects.get(id = profile_id)
    except Profile.DoesNotExist:
        raise Http404()
    try:
        profile_following = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    try:
        profile_followed = Profile.objects.get(id = profile_id)
    except Profile.DoesNotExist:
        raise Http404()
    
    if profile.account_holder==current_user:
        return redirect(my_profile)

    if request.method == 'POST':
        if 'follow' in request.POST:
            form = NewFollowForm(request.POST)
            if form.is_valid():
                this_follow = form.save(commit=False)
                this_follow.followed=profile_followed
                this_follow.follower=profile_following
                this_follow.save()
                set_of_followers=Follow.objects.filter(followed = profile_followed)
                num_of_followers=len(set_of_followers)
                profile_followed.followers=num_of_followers
                profile_followed.save()
                set_of_following=Follow.objects.filter(follower = profile_following)
                num_of_following=len(set_of_following)
                profile_following.following=num_of_following
                profile_following.save()
            return HttpResponseRedirect(f'/userprofile/{profile_id}')
        
        elif 'unfollow' in request.POST:
            form = NewUnfollowForm(request.POST)
            if form.is_valid():
                this_unfollow = form.save(commit=False)
                is_unfollow = Follow.objects.filter(followed = profile_followed, follower = profile_following)
                is_unfollow.delete()                
                set_of_followers=Follow.objects.filter(followed = profile_followed)
                num_of_followers=len(set_of_followers)
                profile_followed.followers=num_of_followers
                profile_followed.save()
                set_of_following=Follow.objects.filter(follower = profile_following)
                num_of_following=len(set_of_following)
                profile_following.following=num_of_following
                profile_following.save()
            return HttpResponseRedirect(f'/userprofile/{profile_id}')



    else:
        form_follow = NewFollowForm()
        form_unfollow = NewUnfollowForm()
    
    images = Image.objects.filter(profile = profile).order_by('-posted')  

    is_following = Follow.objects.filter(followed = profile_followed, follower = profile_following)  

    if is_following:
        return render(request, 'user-profile.html', {"profile": profile, "images": images, "unfollow_form": form_unfollow})

    return render(request, 'user-profile.html', {"profile": profile, "images": images, "follow_form": form_follow})

    


