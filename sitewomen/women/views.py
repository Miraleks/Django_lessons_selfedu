from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import AddPostForm
from .models import Women, Category, TagPost

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    posts = Women.published.all().select_related('cat')

    data = {
        "title": "главная страница",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,

    }

    return render(request, "women/index.html", context=data)


def about(request):
    data = {
        "title": "Это страница о сайте",
        "context": "На этой странице информация о сайте",
    }

    return render(request, "women/about.html", {"data": data, "menu": menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, "women/post.html", data)


def addpage(request):
    form = AddPostForm()
    data = {
        'title': 'Добавление статьи',
        'menu': menu,
        'form': form
    }
    return render(request, "women/addpage.html", data)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

    data = {
        "title": f"Рубрика: {category.name}",
        "menu": menu,
        "posts": posts,
        "cat_selected": category.pk,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


# def categories(request, cat_id):
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')
#
#
# def categories_by_slug(request, cat_slug):
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')
#
#
# def archive(request, year):
#     if year > 2023:
#         # return redirect('/')
#         # return redirect('/', permanent=True)    # путь можно указывать как в тексовом формате
#         # return redirect(index, permanent=True)  # так и в виде функции представления
#         # return redirect("cats", 'music')   # а так же по наименованию адресов в файле urls
#
#         uri = reverse('cats', args=('music', ))
#         # return redirect(uri)
#         # return HttpResponseRedirect(uri)
#         return HttpResponsePermanentRedirect(uri)
#
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>year: {year}</p>')


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)

    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Тэг: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)
