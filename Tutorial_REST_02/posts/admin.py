from django.contrib import admin

# books/admin.py
from .models import Post
admin.site.register(Post)