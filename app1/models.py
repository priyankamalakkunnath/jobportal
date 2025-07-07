from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mentor(models.Model):
    title = models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    
    location=[('Remote','Remote'),
           ('onsite','onsite'),
           ]
    
    joblocation=models.CharField(max_length=20,choices=location)

    experiance=[('any','any'),
           ('today','today'),
            ('2 days ago','2 days ago'),
            ('4 days ago','4 days ago')]
    
    jobexperiance=models.CharField(max_length=20,choices=experiance)

    def __str__(self):
        return f"{self.title} at {self.company}"
class CV(models.Model):
    name = models.CharField(max_length=100)
    cv_file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
        return self.name       
class Event(models.Model):
   

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
   
    time = models.DateTimeField()
    image1 = models.ImageField(upload_to='event_images/')
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    applied = models.BooleanField(default=False)  

    
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')  

class newcontent(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title      
class Newcomment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Newreply(models.Model):
    comment = models.ForeignKey(Newcomment, on_delete=models.CASCADE, related_name='replies')
    reply_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.comment.name}"
class Image(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('design', 'Design'),
        ('graphic', 'Graphic'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.category})"    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.image.name
class BlogImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"    
class register(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    mob=models.IntegerField()
    adress=models.TextField(max_length=50)


    def __str__(self):
        return self.email    
    
class posting(models.Model):

    JOB_TYPE_CHOICES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
]
    email = models.EmailField()
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    job_description = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images/')

    company_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=150, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    facebook_username = models.CharField(max_length=100, blank=True, null=True)
    twitter_username = models.CharField(max_length=100, blank=True, null=True)
    linkedin_username = models.CharField(max_length=100, blank=True, null=True)

    company_logo = models.ImageField(upload_to='company_logos/')

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
class AdminRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email


class Newjobpost(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default='Puma')
    location = models.CharField(max_length=100, default='New York City')
    job_type = models.CharField(max_length=50, default='Full Time')
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)  # optional image

    def __str__(self):
        return self.title

class Applyjob(models.Model):
    job = models.ForeignKey(Newjobpost, on_delete=models.CASCADE)
    user_email = models.EmailField()  # store email instead of User object
    applied_at = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return f"{self.user_email} applied to {self.job.title}"
