from django.contrib import admin
from .models import Post # post불러오기
# Register your models here.

# 관리자이외 수정 불가능
class PostAdminConfig(admin.ModelAdmin):
    list_filter = ['title']

admin.site.register(Post, PostAdminConfig)

