from django.shortcuts import render
from django.views import generic
from .models import Idea 


class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by("-created_on")
    template_name  = 'index.html'
    paginate_by = 1
