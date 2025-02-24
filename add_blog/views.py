from django.http import JsonResponse
from .models import Blog
from django.shortcuts import render
import logging

logger = logging.getLogger('add_blog')

def posts(request):
    if request.path == '/':
        return JsonResponse({'message': 'Добро пожаловать на страницу!'})
    elif request.path == '/posts/':
        data = data_from_database()
        return JsonResponse({'message': 'Успех', 'data': data})

def data_from_database():
    data = Blog.objects.all().values('project_title', 'description', 'username')
    return list(data)
