from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Idea
from .forms import FootNoteForm, IdeaForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)
import requests 


def footnote_delete(request, slug, footnote_id, *args, **kwargs):
    """
    view to delete footnote
    """
    queryset = Idea.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    footnote = post.footnotes.filter(id=footnote_id).first()

    if footnote.name == request.user.username:
        footnote.delete()
        messages.add_message(request, messages.SUCCESS, 'Footnote deleted!')
    else:    # The else seems redundant as option only appears for their own footnote
        messages.add_message(request, messages.ERROR, 'You can only delete your own footnotes, you messer!')
    return HttpResponseRedirect(reverse('idea_detail', args=[slug]))



def footnote_edit(request, slug, footnote_id, *args, **kwargs):
    """
    view to edit footnotes
    """
    if request.method == "POST":

        queryset = Idea.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        footnote = post.footnotes.filter(id=footnote_id).first()

        footnote_form = FootNoteForm(data=request.POST, instance=footnote)

        if footnote_form.is_valid() and footnote.name == request.user.username:
            footnote = footnote_form.save(commit=False)
            footnote.post = post
            footnote.save()
            messages.add_message(request, messages.SUCCESS, 'Footnote Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating footnote!')

    return HttpResponseRedirect(reverse('idea_detail', args=[slug]))


class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 3


class AddIdea(View):
    model = Idea
    template_name = 'add_idea.html'
    idea_form = IdeaForm()

    def get(self, request, *args, **kwargs):
        idea_form = IdeaForm()
        context = {
            "idea_form": idea_form
        }
        return render(request, "add_idea.html", context)
        
    def post(self, request, *args, **kwargs):
        idea_form = IdeaForm(request.POST)
        if idea_form.is_valid():
            idea_form.save()
            messages.success(request, "Your idea has been submitted for approval!")
        else:
            pass
        return redirect('add_idea')
        


class IdeaDetail(View):
    model = Idea                       
    template_name = 'idea_detail.html' 

    def get(self, request, slug, *args, **kwargs):
        queryset = Idea.objects.filter(status=1)
        idea = get_object_or_404(queryset, slug=slug)
        footnotes = idea.footnotes.filter(approved=True).order_by('created_on')
        liked = False
        if idea.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
                request,
                "idea_detail.html",
                {
                    "idea": idea,
                    "footnotes": footnotes,
                    "footnoted": False,
                    "liked": liked,
                    "footnote_form": FootNoteForm()
                },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Idea.objects.filter(status=1)
        idea = get_object_or_404(queryset, slug=slug)
        footnotes = idea.footnotes.filter(approved=True).order_by('created_on')
        liked = False
        if idea.likes.filter(id=self.request.user.id).exists():
            liked = True

        footnote_form = FootNoteForm(data=request.POST)

        if footnote_form.is_valid():
            footnote_form.instance.email = request.user.email 
            footnote_form.instance.name = request.user.username
            footnote = footnote_form.save(commit=False)
            footnote.idea = idea
            footnote.save()
        else:
            footnote_form = FootNoteForm()

        return render(
                request,
                "idea_detail.html",
                {
                    "idea": idea,
                    "footnotes": footnotes,
                    "footnoted": True,
                    "liked": liked,
                    "footnote_form": footnote_form
                },
            ) 
 

class IdeaLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Idea, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('idea_detail', args=[slug]))