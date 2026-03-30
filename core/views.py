from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, About
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    about_info = About.objects.first()
    context = {
        'about': about_info
    }
    return render(request, 'about.html', context)

def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'projects.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully. I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
        
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
