from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path(
        'blog/<int:id>/',
        views.blog_detail,
        name='blog_detail'
    ),

    path(
        'create/',
        views.create_blog,
        name='create_blog'
    ),

    path(
        'edit/<int:id>/',
        views.edit_blog,
        name='edit_blog'
    ),

    path(
        'delete/<int:id>/',
        views.delete_blog,
        name='delete_blog'
    ),

    path(
        'signup/',
        views.signup,
        name='signup'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),
]