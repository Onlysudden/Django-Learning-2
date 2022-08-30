from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Главная страницы'}
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context
    
    def get_queryset(self):
        return Women.objects.filter(is_published=True)

def about(request):
    return render(request, "women/about.html", {"menu": menu, "title": "О сайте"})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def contact(request):
    return HttpResponse("Обратная связь")

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    #success_url = reverse_lazy('home') - Если нету метода get_absolute_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context

def login(request):
    return HttpResponse("Авторизация")

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    #pk_url_kwarg = 'post_pk' Если используется int, например id
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context

class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context
