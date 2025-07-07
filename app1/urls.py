from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path("",views.home, name="home"),
    path('upload/', views.upload_cv, name='upload_cv'),
    path('cv_list', views.cv_list, name='cv_list'),
    path('deletecv/<int:pk>/', views.delete_cv, name='delete_cv'),
    path("rough/",views.rough, name="rough"),
    path('create/', views.create, name='create'),
    
   
    path('vanish/<int:event_id>/', views.deletelist, name='deletelist'),
    path('about/', views.about, name='about'),
    path('upvideo/', views.upload_video, name='upload_video'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    #path('apply/<int:event_id>/', views.apply_job, name='apply_job'),
      path('job/', views.single, name='single'),
    path('single/', views.single, name='single'),

    path('post/', views.post, name='post'),
    path('load/', views.upload_content, name='upload_content'),
    path('content/', views.view_content, name='view_content'),
    path('van/<int:id>/', views.deletelist, name='deletelist'),
    path('single/', views.singleservice, name='singleservice'),
     path('blogsingle/', views.comment_list, name='comment_list'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('img/', views.imgup, name='imgup'),
   path('gallery/delete/<int:image_id>/', views.delete_image, name='delete_image'),
   path('portsingle/', views.portsingle, name='portsingle'),
   path('gal/', views.image_list, name='image_list'),
   path('imgload/', views.image_upload, name='image_upload'),
    path('delete/<int:pk>/', views.image_delete, name='image_delete'),
    
   path('show/', views.show_images, name='show_images'),
    path('uplshow/', views.upload_image, name='upload_image'),
    path('contact/', views.contact, name='contact'),
   path('login/', views.login, name='login'),
   path('reg/', views.Register, name='Register'),
   path('logout/', views.logout, name='logout'),
   path("adreg/", views.adminreg, name="adminreg"),
  path("adlog/", views.adminlogin, name="adminlogin"),
  path("up/", views.uploadjob, name="uploadjob"),
  path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
