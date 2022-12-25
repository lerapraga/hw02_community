from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    '''для главной страницы'''
    posts = Post.objects.all()[:10]
    template = "posts/index.html"
    text = "Это главная страница проекта Yatube"
    context = {
        "posts": posts,
        "text": text
    }
    return render(request, template, context)


def group_posts(request, slug):
    '''для страницы, на которой будут посты, отфильтрованные по группам.'''
    group = get_object_or_404(Group, slug=slug)
    template = "posts/group_list.html"
    text = "Здесь будет информация о группах проекта Yatube"
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        "group": group,
        "posts": posts,
        "text": text
    }
    return render(request, template, context)
