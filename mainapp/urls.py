from django.urls import path,include
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.Index.as_view(), name='index'),
    path('post_create',views.PostCreate.as_view(),name='post_create'),
    path('post_detail/<int:pk>', views.PostDetail.as_view(),name='post_detail'),
    path('post_update/<int:pk>',views.PostUpdate.as_view(),name='post_update'),
    path('post_delete/<int:pk>', views.PostDelete.as_view(),name='post_delete'),
    path('post_list', views.PostList.as_view(),name='post_list'),
    path('login',views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('signup_2242A85', views.SignUp.as_view(), name='signup'),
    path('a_post_create',views.APostCreate.as_view(),name='a_post_create'),
    path('profile',views.Profile.as_view(), name='profile'),
    path('p_post_create',views.ProfilePostCreate.as_view(),name='p_post_create'),
    path('p_post_detail/<int:pk>', views.ProfilePostDetail.as_view(),name='p_post_detail'),
    path('p_post_update/<int:pk>',views.PostProfileUpdate.as_view(),name='p_post_update'),
    path('p_post_delete/<int:pk>', views.PostProfileDelete.as_view(),name='p_post_delete'),
    path('search', views.Search, name='search'),
    path('p_search', views.SearchProfile, name='p_search'),
    path('p_h_search', views.SearchHightoneProfile, name='p_h_search'),
    path('p_m_search', views.SearchMiddletoneProfile, name='p_m_search'),
    path('p_l_search', views.SearchLowtoneProfile, name='p_l_search'),
    path('like/<int:post_id>', views.Like_add, name='like_add'),
    path('like_list', views.LikeList.as_view(),name='like_list'),
]

# /<int:postRecruit_id　の部分は試作段階
# path('m_p_search', views.SearchMyProfile, name='m_p_search'),