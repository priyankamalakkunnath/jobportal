from django.contrib import admin

# Register your models here.
from . models import mentor,CV,Event,Video

from . models import newcontent
from . models import Newreply
from . models import Newcomment
from . models import Image
from . models import GalleryImage
from . models import BlogImage
from . models import Contact
from . models import register
from . models import posting
from . models import Applyjob
from . models import AdminRegister
from .models import Newjobpost




admin.site.register(mentor)
admin.site.register(CV)
admin.site.register(Event)
admin.site.register(Video)
admin.site.register(newcontent)
admin.site.register(Newreply)
admin.site.register(Newcomment)
admin.site.register(Image)
admin.site.register(GalleryImage)
admin.site.register(BlogImage)
admin.site.register(Contact)
admin.site.register(register)
admin.site.register(posting)

admin.site.register(AdminRegister)
admin.site.register(Newjobpost)
admin.site.register(Applyjob)