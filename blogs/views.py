from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Blog, Category, Tag
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#ログインしていないと、create/update/deleteできない様にする
# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = "blogs/home.html"
    context_object_name = 'blogs'
    ordering = ['-date']

    #カテゴリーごとに投稿を拾える様な仕組みにする。
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context.update({
            'blog_random': Blog.objects.all().order_by('?'),
            'blog_travel': Blog.objects.filter(category__name='Travel').order_by('-date'),
            'blog_gourmet': Blog.objects.filter(category__name='Gourmet').order_by('-date'),
            'blog_coding': Blog.objects.filter(category__name='Coding').order_by('-date'),
        })
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"

    #Detail Viewのところで、関連記事を表示したい時のコード
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.all().order_by('?')
        return context
    

class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blogs/blog_form.html'
    form_class = BlogForm

    def upload(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, self.template_name, {'form':form},)

    #今ログインしているユーザーが著者であることを指すためのコード。
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog #これを加えるだけ。
    template_name = 'blogs/blog_form.html'
    form_class = BlogForm

    def upload(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, self.template_name, {'form':form},)
    
    #今ログインしているユーザーが著者であることを指すためのコード。
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): 
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blog_confirm_delete.html'
    form_class = BlogForm
    success_url = '/'

    #Updateと同曜に、ログインユーザーしか削除できない。
    def test_func(self): 
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#カテゴリー表示向け
class CategoryView(ListView):
    model = Blog
    template_name = 'blogs/blog_category.html'

    def get_queryset(self):
        category = Category.objects.get(name=self.kwargs['category'])
        queryset = Blog.objects.order_by('-id').filter(category=category)
        return queryset

    #アクセスした値を取得し辞書に格納
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_key'] = self.kwargs['category']
        return context

#タグ表示向け
class TagView(ListView):
    model = Blog
    template_name = 'blog/index.html'

    def get_queryset(self):
        tag = Tag.objects.get(name=self.kwargs['tag'])
        queryset = Blog.objects.order_by('-id').filter(tag=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_key'] = self.kwargs['tag']
        return context