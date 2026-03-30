from django.contrib import admin
from .models import Project, ContactMessage, About

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'github_link', 'live_link')
    search_fields = ('title', 'technologies', 'description')
    list_filter = ('created_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('name', 'email', 'message', 'created_at')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

