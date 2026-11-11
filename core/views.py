from django.shortcuts import render,  redirect
from django.contrib import messages
from .models import Category, Project, Skill, Experience, Service, ContactMessage, Achievement
from django.urls import reverse


# Create your views here.
# 1. Homepage (Hero + Featured Projects Preview)
def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences= Experience.objects.all()   
    achievements= Achievement.objects.all()
    services= Service.objects.all()   # used in sections/services.html
    context = {
        'projects': projects,   # used in sections/projects.html
        'skills': skills,       # used in sections/skills.html
        'experiences': experiences,   # used in sections/experience.html
        'achievements': achievements,  # used in sections/certificates.html
        'services':services,
    }
    return render(request, 'index.html', context)

# 2. About Page (My Story, Education, Philosophy)
def about(request):
    return render(request, 'about.html')

# 3. Projects Page (Admin ke saare projects yahan load honge)
def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})

# 4. Experience & Achievements Page
def experience(request):
    return render(request, 'experience.html')

# 5. Contact Page (Form Handling with Database Save)

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import ContactMessage


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        # Save only when the required fields are filled
        if name and email and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            messages.success(request, 'Thank you! Your message has been sent successfully. I will get back to you soon.')
        else:
            messages.error(request, 'Please fill in all required fields.')

    # Success, error, and a direct visit to /contact/ all go back to the
    # contact section on the home page (no contact.html template needed)
    return redirect(reverse('home') + '#contact')
       

   
   