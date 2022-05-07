from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.PROTECT,blank=False)
    title = models.CharField('タイトル', max_length=50)
    content = models.TextField('内容', max_length=1000)
    # category = models.ForeignKey('Category', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class PostRecruit(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    song = models.CharField('曲名', max_length=30)
    parts = models.TextField('募集パート', max_length=50)
    comment = models.TextField('コメント', max_length=1000)
    # category = models.ForeignKey('Category', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.song

class Like(models.Model):
    post = models.ForeignKey(PostRecruit, verbose_name="投稿", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Likeしたユーザー", on_delete=models.CASCADE)
    
class PostApplication(models.Model):
    a_author = models.ForeignKey(User, verbose_name="応募したユーザー", on_delete=models.PROTECT, blank=False)
    a_parts = models.TextField('応募パート', max_length=50)
    a_comment = models.TextField('コメント', max_length=1000)
    a_created_at = models.DateTimeField(auto_now_add=True)
    a_target = models.ForeignKey(PostRecruit, on_delete=models.CASCADE, verbose_name="対象の募集")

    def __str__(self):
        return self.a_parts


class PostProfile(models.Model):
    p_author = models.ForeignKey(User, verbose_name="サークルネーム",  on_delete=models.PROTECT, blank=False)
    introduction = models.TextField('自己紹介', max_length=300)
    p_part = models.TextField('主な担当', max_length=200)
    sex = models.ForeignKey('Sex', verbose_name="性別", on_delete=models.PROTECT)
    high = models.ForeignKey('High', verbose_name="高音域", on_delete=models.PROTECT)
    middle = models.ForeignKey('Middle', verbose_name="中音域", on_delete=models.PROTECT)
    low = models.ForeignKey('Low', verbose_name="低音域", on_delete=models.PROTECT)
    freetime = models.TextField('空いている時間', max_length=300)
    p_created_at = models.DateTimeField(auto_now_add=True)
    p_update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.introduction

class Sex(models.Model):
    sex = models.CharField('性別', max_length=10)

    def __str__(self):
        return self.sex


class High(models.Model):
    hightone = models.CharField('高音域', max_length=10)

    def __str__(self):
        return self.hightone


class Middle(models.Model):
    middletone = models.CharField('中音域', max_length=10)

    def __str__(self):
        return self.middletone


class Low(models.Model):
    lowtone = models.CharField('低音域', max_length=10)

    def __str__(self):
        return self.lowtone

