from django.db import models

class Blog(models.Model):
    project_title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=False)
    username = models.CharField(max_length=100, null=True)
    create_post = models.DateTimeField(auto_now_add=True)
    update_post = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_project'
