from django.contrib import admin
from .models import PostApplication, PostRecruit, PostProfile, Sex, High, Middle, Low, Like, LikeProfile


@admin.register(PostRecruit)
class PostAdomin(admin.ModelAdmin):
    list_display = ('id', 'author', 'song', 'parts', 'comment', 'created_at',)
    list_display_links = ('song',)
    ordering = ('-created_at',)

@admin.register(PostApplication)
class APostAdomin(admin.ModelAdmin):
    list_display = ('id','a_author','a_parts', 'a_comment', 'a_created_at',)
    list_display_links = ('a_author',)
    ordering = ('-a_created_at',)

@admin.register(PostProfile)
class PostProfileAdomin(admin.ModelAdmin):
    list_display = ('id','p_author','introduction','p_part','freetime','p_created_at',)
    list_display_links = ('introduction',)
    ordering = ('-p_created_at',)

@admin.register(Sex)
class SexAdomin(admin.ModelAdmin):
    list_display = ('id', 'sex',)
    list_display_links = ('sex',)

@admin.register(High)
class HighAdomin(admin.ModelAdmin):
    list_display = ('id', 'hightone',)
    list_display_links = ('hightone',)

@admin.register(Middle)
class MiddleAdomin(admin.ModelAdmin):
    list_display = ('id', 'middletone',)
    list_display_links = ('middletone',)

@admin.register(Low)
class LowAdomin(admin.ModelAdmin):
    list_display = ('id', 'lowtone',)
    list_display_links = ('lowtone',)

@admin.register(Like)
class LikeAdomin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user',)
    list_display_links = ('post',)

@admin.register(LikeProfile)
class LikeProfileAdomin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'user',)
    list_display_links = ('profile',)