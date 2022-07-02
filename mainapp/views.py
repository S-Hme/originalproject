from re import template
from urllib import request
from django.shortcuts import render,resolve_url
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,DetailView,UpdateView,DeleteView,ListView
from .models import LikeProfile, Post, PostRecruit, PostApplication, PostProfile, Like
from django.urls import reverse_lazy
from .forms import LoginForm, PostApplicationForm, PostForm, PostProfileForm, SearchForm, SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #ログインを義務づける処理、投稿主のみ許可する処理
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required   #defで定義したものに関してはこれを使う

class OnlyMyPostMixin(UserPassesTestMixin): #投稿したユーザーのみが編集できるようにする処理
    raise_exception = True
    def test_func(self):
        post = PostRecruit.objects.get(id = self.kwargs['pk'])
        return post.author == self.request.user

class OnlyMyProfileMixin(UserPassesTestMixin): #投稿したユーザーのみが編集できるようにする処理
    raise_exception = True
    def test_func(self):
        post = PostProfile.objects.get(id = self.kwargs['pk'])
        return post.p_author == self.request.user

class Index(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        post_list = PostRecruit.objects.all().order_by('-update_at')
        context = {
            'post_list': post_list, 
        }
        return context

    # def confirmation_like(request,post_id):
    #     is_liked = Like.objects.filter(user = request.user, post = post_id).count()
    #     return is_liked


class PostCreate(LoginRequiredMixin, CreateView): #投稿するときの処理
    model = PostRecruit
    form_class = PostForm
    success_url = reverse_lazy('mainapp:index')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, '募集を投稿しました。')
        return resolve_url('mainapp:index')

class PostDetail(DetailView): #投稿の詳細画面を定義
    model = PostRecruit

    def a_get_context_data(self, *args,**kwargs):
        a_context = super().a_get_context_data(**kwargs)
        a_post_list = PostApplication.objects.all().order_by('-a_created_at')
        a_context = {
            'a_post_list': a_post_list, 
        }
        return a_context

    #def get_context_data(self, *args, **kwargs):
    #    detail_data = Post.objects.get(id = self.kwargs['pk'])
    #    category_posts = Post.objects.filter(category = detail_data.category).order_by('-created_at')[:5]
    #    params = {
    #        'object': detail_data,
    #        'category_posts': category_posts,
    #    }
    #   return params

class PostUpdate(OnlyMyPostMixin, UpdateView): #投稿を更新する処理
    model = PostRecruit
    form_class = PostForm

    def get_success_url(self):
        messages.info(self.request,'投稿を更新しました')
        return resolve_url('mainapp:post_detail', pk=self.kwargs['pk'])

class PostDelete(OnlyMyPostMixin, DeleteView): #投稿を削除する処理
    model = PostRecruit

    def get_success_url(self):
        messages.info(self.request, '投稿を削除しました。')
        return resolve_url('mainapp:index')

class PostList(ListView):
    model = PostRecruit
    paginate_by = 5

    def get_queryset(self):
        return PostRecruit.objects.all().order_by('-update_at')

@login_required
def Like_add(request,post_id):  #お気に入りを登録する処理
    post = PostRecruit.objects.get(id = post_id)
    
    is_liked = Like.objects.filter(user = request.user, post = post_id).count()

    if is_liked > 0:  #お気に入りから削除する処理

        liked = Like.objects.filter(user = request.user, post = post_id)
        liked.delete()
        messages.info(request,'お気に入りから削除しました')

    if is_liked == 0: #お気に入りに登録する処理

        like = Like()
        like.user = request.user
        like.post = post
        like.save()
        messages.success(request,'お気に入りに追加しました')

    return redirect('mainapp:post_detail', post.id)


class LikeList(ListView):
    model = PostRecruit
    template_name = 'mainapp/like_list.html'

    def get_queryset(self):

        # a = Like.objects.all().filter(user = self.request.user)
        # return a
        # PostRecruit.objects.all().filter(song = a.post)
        return Like.objects.all().filter(user = self.request.user)

# ////////////////////////////////////////////////////////////////////////////

# @login_required
# def Like_add(request,post_id):
#     post = PostRecruit.objects.get(id = post_id)
#     is_like = Like.objects.filter(User=request.user).filter(post=post).count()
#     #unlike
#     if is_like == 1:
#         like = Like.objects.filter(User=request.user.id).filter(post=post)
#         like.delete()
#         post.count -= 1
#         post.save()

#         messages.success(request,'お気に入りから削除しました')

#         return redirect('mainapp:postRecruit_detail', post.id)
#     #like
#     if is_like == 0:
#         post.count += 1
#         post.save()
#         Like.objects.create(User=request.user, post=post)

#         messages.success(request,'お気に入りに追加しました')

#         return redirect('mainapp:postRecruit_detail', post.id)

# //////////////////////////////////////////////////////////////////////////////////

class Login(LoginView):
    form_class = LoginForm
    template_name = 'mainapp/login.html'

class Logout(LogoutView):
    template_name = 'mainapp/logout.html'

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'mainapp/signup.html'
    success_url = reverse_lazy('mainapp:index')

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        self.object = user
        messages.info(self.request, 'ユーザー登録をしました。')
        return HttpResponseRedirect(self.get_success_url())



class APostCreate(LoginRequiredMixin, CreateView): #投稿するときの処理
    form_class = PostApplicationForm
    success_url = reverse_lazy('mainapp:index')

    def form_valid(self,form,post_id): 
        
        post = PostRecruit.objects.get(id = post_id)

        application = PostApplication()
        application.a_target = post
        application.save()
        form.instance.a_author_id = self.request.user.id
        return super(APostCreate, self).form_valid(form)


    def a_get_success_url(self):
        messages.success(self.request, '募集に応募しました。')
        return resolve_url('mainapp:index')


# class AIndex(TemplateView):
#     template_name = 'mainapp/postRecruit_detail.html'

#     def a_get_context_data(self, *args,**kwargs):
#         a_context = super().a_get_context_data(**kwargs)
#         a_post_list = PostApplication.objects.all().order_by('-a_created_at')
#         a_context = {
#             'a_post_list': a_post_list, 
#         }
#         return a_context



    # def A_add(request,post_id):  #お気に入りを登録する処理
    #     post = PostRecruit.objects.get(id = post_id)
        
    #     is_liked = PostApplication.objects.filter(user = request.user, post = post_id).count()
    #     if is_liked > 0:  #同じ投稿を何度もお気に入りに追加できないようにする処理
    #         messages.info(request,'すでにお気に入りに追加済みです')
    #         return redirect('mainapp:post_detail', post.id)

    #     like = PostApplication()
    #     like.user = request.user
    #     like.post = post
    #     like.save()

    #     messages.success(request,'お気に入りに追加しました')
    #     return redirect('mainapp:post_detail', post.id)

class Profile(TemplateView): #
    template_name = 'mainapp/profile.html'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        post_list = PostProfile.objects.all().order_by('-p_update_at')
        context = {
            'post_list': post_list, 
        }
        return context

class ProfilePostCreate(LoginRequiredMixin, CreateView): #投稿するときの処理
    model = PostProfile
    form_class = PostProfileForm
    success_url = reverse_lazy('mainapp:profile')

    def form_valid(self, form):
        form.instance.p_author_id = self.request.user.id
        return super(ProfilePostCreate, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'プロフィールを投稿しました。')
        return resolve_url('mainapp:profile')

class ProfilePostDetail(DetailView): #プロフィールの詳細画面を定義
    model = PostProfile

def Search(request):
    if request.method == 'POST':
        searchform = SearchForm(request.POST)

        if searchform.is_valid():
            freeword = searchform.cleaned_data['freeword']
            search_list = PostRecruit.objects.filter(Q(author__username = freeword)|Q(song__icontains = freeword)|Q(parts__icontains = freeword)|Q(comment__icontains = freeword)|Q(praTime__icontains = freeword))

        params = {
            'search_list': search_list,
        }

        return render (request, 'mainapp/searchRecruit.html', params)

class PostProfileUpdate(OnlyMyProfileMixin, UpdateView): #投稿を更新する処理
    model = PostProfile
    form_class = PostProfileForm

    def get_success_url(self):
        messages.info(self.request,'プロフィールを更新しました')
        return resolve_url('mainapp:p_post_detail', pk=self.kwargs['pk'])

class PostProfileDelete(OnlyMyProfileMixin, DeleteView): #投稿を削除する処理
    model = PostProfile

    def get_success_url(self):
        messages.info(self.request, 'プロフィールを削除しました。')
        return resolve_url('mainapp:profile')

@login_required
def Like_profile_add(request,post_id):  #お気に入りを登録する処理
    profile = PostProfile.objects.get(id = post_id)
    
    is_liked = LikeProfile.objects.filter(user = request.user, profile = post_id).count()

    if is_liked > 0:  #お気に入りから削除する処理

        liked = LikeProfile.objects.filter(user = request.user, profile = post_id)
        liked.delete()
        messages.info(request,'お気に入りから削除しました')

    if is_liked == 0: #お気に入りに登録する処理

        like = LikeProfile()
        like.user = request.user
        like.profile = profile
        like.save()
        messages.success(request,'お気に入りに追加しました')

    return redirect('mainapp:p_post_detail', post_id)


class LikeProfileList(ListView):
    model = PostProfile
    template_name = 'mainapp/likeProfile_list.html'

    def get_queryset(self):

        # a = Like.objects.all().filter(user = self.request.user)
        # return a
        # PostRecruit.objects.all().filter(song = a.post)
        return LikeProfile.objects.filter(user = self.request.user)

        # .filter(user = self.request.user)


def SearchProfile(request):
    if request.method == 'POST':
        searchform = SearchForm(request.POST)

        if searchform.is_valid():
            freeword = searchform.cleaned_data['freeword']
            search_list = PostProfile.objects.filter(Q(p_author__username__icontains = freeword)|Q(sex__sex__icontains = freeword)|Q(p_part__icontains = freeword)|Q(freetime__icontains = freeword))

        params = {
            'search_list': search_list,
        }

        return render (request, 'mainapp/searchProfile.html', params)

def SearchHightoneProfile(request):
    
    freeword = '得意'
    search_list = PostProfile.objects.filter(Q(high__hightone__icontains = freeword))

    params = {
        'search_list': search_list,
    }

    return render (request, 'mainapp/searchProfile.html', params)


def SearchMiddletoneProfile(request):
    
    freeword = '得意'
    search_list = PostProfile.objects.filter(Q(middle__middletone__icontains = freeword))

    params = {
        'search_list': search_list,
    }

    return render (request, 'mainapp/searchProfile.html', params)


def SearchLowtoneProfile(request):
    
    freeword = '得意'
    search_list = PostProfile.objects.filter(Q(low__lowtone__icontains = freeword))

    params = {
        'search_list': search_list,
    }

    return render (request, 'mainapp/searchProfile.html', params)

# def SearchMyProfile(request):
#     searchform = SearchMyProfileForm(request.POST)

#     if searchform.is_valid():
#         freeword = searchform.cleaned_data['freeword']
#         search_list = PostProfile.objects.filter(Q(p_author__username = freeword))

#     params = {
#         'search_list': search_list,
#     }

#     return render (request, 'mainapp/searchProfile.html', params)
