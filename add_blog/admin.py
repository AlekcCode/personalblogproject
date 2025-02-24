from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'description', 'username', 'create_post', 'update_post')
    search_files = ('username', 'project_title')
    filter_files = ('username', 'create_post', 'update_post')