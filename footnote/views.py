from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Idea
from .forms import FootNoteForm


class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by("-created_on")
    template_name  = 'index.html'
    paginate_by = 1

class IdeaDetail(View):

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
                "liked": liked,
                "footnote_form": FootNoteForm()
            },
        )
        