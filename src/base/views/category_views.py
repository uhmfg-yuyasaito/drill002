from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Category


class CategoryIndexListView(ListView):
    model = Category
    template_name = 'pages/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category'
        context['template_path'] = 'snippets/category_box.html'
        return context