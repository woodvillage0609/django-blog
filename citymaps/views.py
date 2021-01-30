from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import City, Completion, Tag
from .forms import CityForm
from account.models import Account
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CityListView(ListView):
    model = City
    template_name = "citymaps/index.html"
    context_object_name = 'citymaps'
    ordering = ['-date']

class CityDetailView(DetailView):
    model = City
    template_name = "citymaps/map_detail.html"

    #Detail Viewのところで、関連記事を表示したい時のコード
    def get_context_data(self, **kwargs):
        context = super(CityDetailView, self).get_context_data(**kwargs)
        context.update({
            'citymap_list': City.objects.all().order_by('?'),
            'blog_profile':Account.objects.filter(pk=1),
        })
        return context


class CityCreateView(LoginRequiredMixin, CreateView):
    template_name = 'citymaps/citymap_form.html'
    form_class = CityForm

    def upload(self, request):
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, self.template_name, {'form':form},)

    #今ログインしているユーザーが著者であることを指すためのコード。
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = City #これを加えるだけ。
    template_name = 'citymaps/citymap_form.html'
    form_class = CityForm

    def upload(self, request):
        form = CityForm(request.POST, request.FILES)
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

class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'citymaps/citymap_confirm_delete.html'
    form_class = CityForm
    success_url = '/'

    #Updateと同曜に、ログインユーザーしか削除できない。
    def test_func(self): 
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False