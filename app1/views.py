from django.shortcuts import render,redirect,get_object_or_404
from .models import mentor
from .models import CV
from .models import Event
from django.utils.dateparse import parse_datetime
from .models import Video
from .models import newcontent
from .models import Newreply
from .models import Newcomment
from .models import Image
from .models import GalleryImage
from .models import BlogImage
from datetime import date
from .models import Contact
from django.contrib import messages
from .models import register
from .models import posting
from django.contrib.auth.decorators import login_required
from .models import Applyjob
from .models import AdminRegister
from .models import Newjobpost
def home(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    if request.session.get("admin_email"):
        context["is_admin"] = True
    else:
        context["is_admin"] = False
        context["current_user"] = request.session.get("email")

    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        joblocation = request.POST.get('location')
        jobexperiance = request.POST.get('experiance')

        mentor.objects.create(
            title=title,
            company=company,
            joblocation=joblocation,
            jobexperiance=jobexperiance
        )

    return render(request, 'home.html', context)
def upload_cv(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cv_file = request.FILES.get('cv_file')

        if name and cv_file:
            CV.objects.create(name=name, cv_file=cv_file)
            return redirect('cv_list')

    return render(request, 'cv.html')
def cv_list(request):
    cvs = CV.objects.all()
    return render(request, 'cvnew.html', {'cvs': cvs})

def delete_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    cv.cv_file.delete()  # delete the file from storage
    cv.delete()
    return redirect('cv_list')
def rough(request):
    events = Event.objects.all()
    return render(request,"rough.html" ,{'events': events})
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        location = request.POST.get('location')
        payment = request.POST.get('payment')
        time = request.POST.get('time')
        image1 = request.FILES.get('image1')

        Event.objects.create(
            title=title,
            subtitle=subtitle,
            location=location,
            payment=payment,
            time=parse_datetime(time),
            image1=image1,
        )
        return redirect('home',) 
    
     # or redirect('event') if you want to show list after create

    return render(request, 'event_form.html')
def deletelist(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # changed from Photo to Event
    if event.image1:
        event.image1.delete()  # deletes the image file
    event.delete()  # deletes the database record
    return redirect('home')

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video_file = request.FILES.get('video_file')
        if video_file and title:
            Video.objects.create(title=title, video_file=video_file)
            return redirect('about')
    return render(request, 'video.html')
def about(request):
    videos = Video.objects.all()
    return render(request, "about.html", {'videos': videos})
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == "POST":
        video.delete()
    return redirect('upload_video')

'''def single(request):
        events = Event.objects.all()
        return render(request,"job.html" ,{'events': events})'''
def post(request):
    return render(request,"post.html")

def upload_content(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')

        if title and paragraph and image:
            newcontent.objects.create(title=title, paragraph=paragraph, image=image)
            return redirect('view_content')
    return render(request, 'newservice.html')

def upload_content(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')

        if title and paragraph and image:
            newcontent.objects.create(title=title, paragraph=paragraph, image=image)
            return redirect('view_content')
    return render(request, 'newservice.html')

def view_content(request):
    contents = newcontent.objects.all()
    return render(request, 'service.html', {'contents': contents})

def deletelist(request, id):
    content = get_object_or_404(newcontent, id=id)
    content.delete()
    return redirect('view_content')
def singleservice(request):
    return render(request,"singleservice.html")

def comment_list(request):
    context = {}

    if request.method == 'POST':
        # Handle new comment
        if 'submit_comment' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            website = request.POST.get('website', '')
            message = request.POST.get('message')

            if name and email and message:
                Newcomment.objects.create(
                    name=name,
                    email=email,
                    website=website,
                    message=message
                )
                return redirect('comment_list')
            else:
                context['error'] = "Please fill all required comment fields."

        # Handle reply
        elif 'submit_reply' in request.POST:
            reply_text = request.POST.get('reply_text')
            comment_id = request.POST.get('comment_id')

            if reply_text and comment_id:
                try:
                    comment = Newcomment.objects.get(id=comment_id)
                    Newreply.objects.create(reply_text=reply_text, comment=comment)
                except Newcomment.DoesNotExist:
                    context['reply_error'] = "Comment not found."
                return redirect('comment_list')
            else:
                context['reply_error'] = "Reply cannot be empty."

    # Data for display
    comments = Newcomment.objects.prefetch_related('replies').order_by('-created_at')

    context.update({
        'comments': comments,
        'page_title': "Blog | Comments & Replies",
        'total_comments': comments.count(),
        'latest_comment': comments.first(),
    })

    return render(request, 'blogsingle.html', context)
def portfolio(request):
    selected_category = request.GET.get('category', 'all')

    if selected_category == 'all':
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category=selected_category)

    return render(request, 'portfolio.html', {
        'images': images,
        'selected_category': selected_category,
    })  
    


def imgup(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        if title and category and image:
            Image.objects.create(title=title, category=category, image=image)
            return redirect('portfolio')  # ✅ redirect to gallery after upload

    return render(request, "img.html") 
def portfolio(request):
    selected_category = request.GET.get('category', 'all')

    if selected_category == 'all':
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category=selected_category)

    return render(request, 'portfolio.html', {
        'images': images,
        'selected_category': selected_category,
    })
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('image_gallery')
def portsingle(request):
    return render(request,"portsingle.html")

def image_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def image_upload(request):
    if request.method == 'POST' and request.FILES.get('image'):
        img = request.FILES['image']
        GalleryImage.objects.create(image=img)
        return redirect('image_list')
    return render(request, 'imageupload.html')

def image_delete(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        image.image.delete()  # delete file from disk
        image.delete()        # delete from DB
        return redirect('image_list')
    return render(request, 'imageupload.html', {'image': image})

def upload_image(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        today = date.today()

        if title and image:
            BlogImage.objects.create(title=title, image=image, date=today)
            return redirect('show_images')

    return render(request, 'blogupload.html')

def show_images(request):
    images = BlogImage.objects.all()
    return render(request, 'blog.html', {'images': images})
def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate fields
        if not all([first_name, last_name, email, subject, message]):
            messages.error(request, "All fields are required.")
            return redirect('contact')

        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Message sent successfully.")
        return redirect('contact')

    return render(request, 'contact.html')
def login(request):
    print("jjjjjjjjjjjjjjjjj")
    if request.method == "POST":
        print("rrrrrrrrrrrrrrrrrrrr")
        email = request.POST["email"]
        password = request.POST["psw"] 
        # Find user by email and authenticate
        try:
            user=register.objects.filter(email=email,password=password)
            print("yyyyyyyyyyyyyyy")
            if user:
                request.session["email"]=email
                return redirect("home")
            else:
                messages.error(request, "Invalid password.") # If password doesn&#39;t match
                
        except register.DoesNotExist:
           messages.error(request, "User not found.") # If no user with that email
    return render(request, 'login.html')
def Register(request):
    if request.method == "POST":
        name=request.POST["name"]
        email = request.POST["email"]
        password = request.POST["psw"]
        mob=request.POST["mob"]
        adress=request.POST["adress"]
        
        if register.objects.filter(email=email).exists():
           messages.error(request, "Email already registered")
        else:
           register.objects.create(name=name,email=email,password=password,mob=mob,adress=adress)
           return redirect("home")

    return render(request, "register.html")   
    


def post(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        job_title = request.POST.get('job_title')
        location = request.POST.get('location')
        region = request.POST.get('region')
        job_type = request.POST.get('job_type')
        job_description = request.POST.get('job_description')
        featured_image = request.FILES.get('featured_image')

        company_name = request.POST.get('company_name')
        tagline = request.POST.get('tagline')
        company_description = request.POST.get('company_description')
        website = request.POST.get('website')

        facebook = request.POST.get('facebook_username')
        twitter = request.POST.get('twitter_username')
        linkedin = request.POST.get('linkedin_username')

        company_logo = request.FILES.get('company_logo')

        posting.objects.create(
            email=email,
            job_title=job_title,
            location=location,
            region=region,
            job_type=job_type,
            job_description=job_description,
            featured_image=featured_image,
            company_name=company_name,
            tagline=tagline,
            company_description=company_description,
            website=website,
            facebook_username=facebook,
            twitter_username=twitter,
            linkedin_username=linkedin,
            company_logo=company_logo
        )
        return redirect('home')  # redirect to success page or wherever you want

    return render(request, 'post.html')
def adminreg(request):
    if request.method == "POST":
        name=request.POST["name"]
        email = request.POST["email"]
        password = request.POST["psw"]
        
        
        if AdminRegister.objects.filter(email=email).exists():
           messages.error(request, "Email already registered")
        else:
           AdminRegister.objects.create(name=name,email=email,password=password)
           return redirect("home")

    return render(request, "admin.html")   
def adminlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("psw")

        try:
            admin = AdminRegister.objects.get(email=email)
            if admin.password == password:
                # Store email in session
                request.session["admin_email"] = admin.email
                messages.success(request, "Login successful!")
                return redirect("home")  # change this to your dashboard URL name
            else:
                messages.error(request, "Invalid password.")
        except AdminRegister.DoesNotExist:
            messages.error(request, "Email not registered.")

    return render(request, "adminlogin.html")

def logout(request):
    # Clear all session data
    request.session.flush()
    return redirect('home')  
def uploadjob(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        job_type = request.POST.get('job_type')
        image = request.FILES.get('image')

        Newjobpost.objects.create(
            title=title,
            company=company,
            location=location,
            job_type=job_type,
            image=image
        )
        return redirect('home')

    return render(request, 'upload.html')


def apply_for_job(request, job_id):
    # Custom login session check
    if not request.session.get("email"):
        return redirect("login")

    job = get_object_or_404(Newjobpost, id=job_id)
    user_email = request.session["email"]

    # Save application if not already applied
    if not Applyjob.objects.filter(job=job, user_email=user_email).exists():
        Applyjob.objects.create(job=job, user_email=user_email)
        print("✅ Saved:", user_email, "->", job.title)
    else:
        print("⚠️ Already applied:", user_email)

    return redirect("single")

def single(request):
    events = Event.objects.all()  # This line is safe even if not used in the template
    jobs = Newjobpost.objects.all()
    applied_job_ids = []

    if request.session.get("email"):
        applied_job_ids = Applyjob.objects.filter(
            user_email=request.session["email"]
        ).values_list('job_id', flat=True)

    return render(request, "job.html", {
        'events': events,  # Optional, for future use
        'jobs': jobs,
        'applied_job_ids': applied_job_ids
    })
