from django import forms
from .models import Profile, Image, Comment, Follow

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['created', 'account_holder', 'followers', 'following']

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['posted', 'profile', 'likes']

class NewFollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']

class NewUnfollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']
