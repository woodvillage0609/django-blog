from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import City, Completion, Tag
from .forms import CityForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CityListView(ListView):
    model = City
    template_name = "citymaps/index.html"
    context_object_name = 'citymaps'
    ordering = ['-date']

class CityDetailView(DetailView):
    model = City
    template_name = "citymaps/map_detail.html"


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