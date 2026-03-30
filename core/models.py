from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=255, help_text="Comma-separated technologies used (e.g. Django, Bootstrap, PostgreSQL)")
    github_link = models.URLField(max_length=200, blank=True, null=True)
    live_link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
        
    class Meta:
        ordering = ['-created_at']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.email}"
        
    class Meta:
        ordering = ['-created_at']

class About(models.Model):
    title = models.CharField(max_length=200, default="Who am I?")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True, help_text="Upload your profile picture here")
    bio_intro = models.TextField(help_text="The first introductory paragraph for the about me section.", blank=True)
    bio_details = models.TextField(help_text="The main details to go after the intro.", blank=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Upload your Resume/CV here")
    
    def __str__(self):
        return "About Me Section"
