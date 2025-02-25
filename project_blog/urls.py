from django.urls import path
from django.contrib import admin
from add_blog.views import HomeView, PostView, PostViewDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('posts/', PostView.as_view(), name='posts'),
    path('posts/<int:id>/', PostViewDetail.as_view(), name='posts_detail')
]
