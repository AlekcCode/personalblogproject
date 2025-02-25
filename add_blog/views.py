from Tools.scripts.make_ctype import method
from django.http import JsonResponse
from .models import Blog
from django.shortcuts import render
import logging

logger = logging.getLogger('add_blog')

def posts(request, id=None):
    if request.path == '/':
        return JsonResponse({'message': 'Добро пожаловать на страницу!'})
    elif request.path == '/posts/':
        data = data_from_database()
        return JsonResponse({'message': 'Успех', 'data': data})
    elif id is not None:
        try:
            post = Blog.objects.get(id=id)
            data = {
                'id': post.id,
                'project_title': post.project_title,
                'description': post.description,
                'username': post.username,
            }
            return JsonResponse({'message': 'Успех', 'data': data})
        except Blog.DoesNotExist:
            return JsonResponse({'message': 'Пост не найден'}, status=404)
    else:
        return JsonResponse({'message': 'Неверный запрос'}, status=400)


def data_from_database():
    data = Blog.objects.all().values('id', 'project_title', 'description', 'username')
    return list(data)
