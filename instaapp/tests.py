from django.test import TestCase
from .models import Profile, Image, Comment, Follow, Like
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.this_user =User.objects.create_user('mimi', 'mimi@gmail.com', 'moringa')        
        self.this_profile = Profile(bio='bio', account_holder= self.this_user)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_profile,Profile))

    # Testing Save Method
    def test_save_profile_method(self):
        self.this_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    # Testing Delete Method
    def test_delete_profile_method(self):
        self.this_profile.save_profile()
        profile = Profile.objects.get(bio ='bio')
        profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    # Testing Update Method
    def test_update_profile_method(self):        
        self.this_profile.save_profile()
        profile = Profile.objects.get(account_holder = self.this_user)        
        profile.bio = 'otherBio'
        profile.update_profile()
        query_set = Profile.objects.all()[:1]
        updated_profile=None
        for prof in query_set:
            updated_profile = prof
        self.assertEqual(updated_profile.bio, 'otherBio')
    

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.this_user =User.objects.create_user('mimi', 'mimi@gmail.com', 'moringa')        
        self.this_profile = Profile(bio='bio', account_holder= self.this_user)
        self.this_profile.save_profile()
        self.this_image = Image(image_name='myimage', caption='mycaption', profile = self.this_profile)

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_image,Image))


    # Testing Save Method
    def test_save_image_method(self):
        self.this_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing Delete Method
    def test_delete_image_method(self):
        self.this_image.save_image()
        image = Image.objects.get(caption ='mycaption')
        image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    # Testing Update Method
    def test_update_caption_method(self):        
        self.this_image.save_image()
        image = Image.objects.get(caption ='mycaption')        
        image.image_name = 'otherName'
        image.update_caption()
        query_set = Image.objects.all()[:1]
        updated_image=None
        for img in query_set:
            updated_image = img
        self.assertEqual(updated_image.image_name, 'otherName')