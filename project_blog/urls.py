from django.contrib import admin
from django.urls import path
from add_blog.views import posts


urlpatterns = [
    path('', posts),
    path('admin/', admin.site.urls),
    path('posts/', posts, name='posts'),
    path('posts/<id>/', posts, name='posts_detail')
]
