from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^home/$',views.home,name = 'home'),
    url(r'^sendemail/$',views.send_email,name = 'send-email'),
    url(r'^createprofile/$',views.create_profile,name = 'create-profile'),
    url(r'^myprofile/$',views.my_profile,name = 'my-profile'),
    url(r'^uploadimage/$',views.upload_image,name = 'upload-image'),
    url(r'^deleteimage/(\d+)',views.delete_image,name = 'delete-image'),
    url(r'^updatecaption/(\d+)',views.update_caption,name = 'update-caption'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)