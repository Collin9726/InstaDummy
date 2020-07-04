from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(upload_to = 'profilepics/', blank=True)
    bio = models.TextField()
    account_holder = models.ForeignKey(User,on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.bio 

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()


class Image(models.Model):    
    posted = models.DateTimeField(auto_now_add=True)
    url = models.ImageField(upload_to = 'posts/')
    name = models.CharField(max_length =30)
    caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.update(caption = new_caption)



class Comment(models.Model): 
    posted = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text 

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def update_comment(self):
        self.save()

    