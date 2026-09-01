from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import BlogPost
from .forms import BlogPostForm


def home(request):

    search = request.GET.get('search')

    if search:
        posts = BlogPost.objects.filter(
            title__icontains=search
        )
    else:
        posts = BlogPost.objects.all()

    return render(request, 'blog/home.html', {
        'posts': posts
    })


def blog_detail(request, id):

    post = get_object_or_404(BlogPost, id=id)

    return render(request, 'blog/blog_detail.html', {
        'post': post
    })


@login_required
def create_blog(request):

    if request.method == 'POST':

        form = BlogPostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()

            messages.success(
                request,
                'Blog created successfully!'
            )

            return redirect('home')

    else:
        form = BlogPostForm()

    return render(request, 'blog/create_blog.html', {
        'form': form
    })


@login_required
def edit_blog(request, id):

    post = get_object_or_404(
        BlogPost,
        id=id,
        author=request.user
    )

    if request.method == 'POST':

        form = BlogPostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Blog updated successfully!'
            )

            return redirect('blog_detail', id=post.id)

    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/edit_blog.html', {
        'form': form,
        'post': post
    })


@login_required
def delete_blog(request, id):

    post = get_object_or_404(
        BlogPost,
        id=id,
        author=request.user
    )

    if request.method == 'POST':

        post.delete()

        messages.success(
            request,
            'Blog deleted successfully!'
        )

        return redirect('home')

    return render(request, 'blog/delete_blog.html', {
        'post': post
    })


def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            messages.error(
                request,
                'Passwords do not match!'
            )

            return redirect('signup')

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists!'
            )

            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(
            request,
            'Account created successfully! Please login.'
        )

        return redirect('login')

    return render(request, 'blog/signup.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f'Welcome {user.username}!'
            )

            return redirect('home')

        else:

            messages.error(
                request,
                'Invalid username or password!'
            )

    return render(request, 'blog/login.html')


def user_logout(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out successfully!'
    )

    return redirect('home')