from .models import Blog
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer

logger = logging.getLogger('add_blog')


class PostView(APIView):
    def get(self, request):
        posts = Blog.objects.all()
        serializer = BlogSerializer(posts, many=True)
        return Response({'status': 'успех', 'data': serializer.data})


class PostViewDetail(APIView):
    def get(self, request, id=None):
        try:
            post = Blog.objects.get(id=id)
            serializer = BlogSerializer(post)
            return Response({'status': 'успех', 'data': serializer.data})
        except Blog.DoesNotExist:
            return Response({'status': 'failed', 'message': 'Пост не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': 'failed', 'message': f'Ошибка: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HomeView(APIView):
    def get(self, request):
        return Response({'status': 'Успех', 'message': 'Добро пожаловать на страницу!'})
