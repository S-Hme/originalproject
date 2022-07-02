from django.contrib import admin
from .models import PostApplication, PostRecruit, PostProfile, Sex, High, Middle, Low, Like, LikeProfile


@admin.register(PostRecruit)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'song', 'parts', 'comment','praTime', 'created_at','update_at',)
    list_display_links = ('song',)
    ordering = ('-update_at',)

@admin.register(PostApplication)
class APostAdmin(admin.ModelAdmin):
    list_display = ('id','a_author','a_parts', 'a_comment', 'a_created_at',)
    list_display_links = ('a_author',)
    ordering = ('-a_created_at',)

@admin.register(PostProfile)
class PostProfileAdmin(admin.ModelAdmin):
    list_display = ('id','p_author','introduction','p_part','freetime','p_created_at','p_update_at',)
    list_display_links = ('introduction',)
    ordering = ('-p_update_at',)

@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('id', 'sex',)
    list_display_links = ('sex',)

@admin.register(High)
class HighAdmin(admin.ModelAdmin):
    list_display = ('id', 'hightone',)
    list_display_links = ('hightone',)

@admin.register(Middle)
class MiddleAdmin(admin.ModelAdmin):
    list_display = ('id', 'middletone',)
    list_display_links = ('middletone',)

@admin.register(Low)
class LowAdmin(admin.ModelAdmin):
    list_display = ('id', 'lowtone',)
    list_display_links = ('lowtone',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user',)
    list_display_links = ('post',)

@admin.register(LikeProfile)
class LikeProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'user',)
    list_display_links = ('profile',)