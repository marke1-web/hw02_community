from django.shortcuts import render, get_object_or_404

from .models import Group, Post
POST_COUNT_PER_PAGE = 10


def index(request):
    posts = Post.objects.all()[:POST_COUNT_PER_PAGE]
    context = {
        'posts': posts,
        'title': "Последние обновления на сайте"
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:POST_COUNT_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
        'title': f"Записи сообщества {group}"
    }
    return render(request, 'posts/group_list.html', context)
