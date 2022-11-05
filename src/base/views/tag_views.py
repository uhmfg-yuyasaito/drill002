from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Tag


class TagIndexListView(ListView):
    model = Tag
    template_name = 'pages/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tag'
        context['template_path'] = 'snippets/tag_box.html'
        return context