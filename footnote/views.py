from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Idea, FootNote
from .forms import FootNoteForm, IdeaForm
from django.views.generic import ListView

class AddIdea(View):
    model = Idea
    template_name = 'add_idea.html'
#    fields = '__all__' NOT SURE DO WE NEED TO STIPULATE FIELDS

    def post(self, request):
        if request.method == 'POST': 
            idea_form = IdeaForm(request.POST)
            if idea_form.is_valid():
                idea_form.save()
                return redirect('idea_detail')
        idea_form = IdeaForm()
        context = {
            'idea_form': idea_form
         }   
        return render(request, self.template_name, context)

class EditIdea(View):
    model = Idea
    template_name = 'edit_idea.html'

    def edit_idea(self, request, slug): # SLUG INSTEAD OF ID
        idea = get_object_or_404(Idea, slug=slug)
        if request.method == 'POST': 
            idea_form = IdeaForm(data=request.POST, instance=idea)
            if idea_form.is_valid():
                idea_form.save()
                return redirect('idea_detail')
        idea_form = IdeaForm(instance=idea)
        context = {
            'idea_form': idea_form
         } 
        return render(request, self.template_name, context)

class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 3

class IdeaDetail(View):
    model = Idea                       #IS THIS NEEDED
    template_name = 'idea_detail.html' #IS THIS NEEDED

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
                    "footnoted":True,
                    "liked": liked,
                    "footnote_form": FootNoteForm()
                },
            ) 

class DeleteIdea(View):
    model = Idea                       #IS THIS NEEDED
    template_name = 'idea_detail.html' #IS THIS NEEDED

    def delete_idea(self, request, slug): # SLUG INSTEAD OF ID
            idea = get_object_or_404(Idea, slug=slug) #SLUG OR ID TO BE USED IN VIEW
            idea.delete()
            return render(request, self.template_name, args=[slug]) #Not sure if args is needed

class IdeaLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Idea, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('idea_detail', args=[slug]))

#class FootNoteLike(View): #What id can be used for footnotes-no slug

#    def post(self, request, footnote_id):
#        post = get_object_or_404(FootNote, id=footnote_id)

#        if post.likes.filter(id=request.user.id).exists():
#            post.likes.remove(request.user)
#        else:
#            post.likes.add(request.user)

#        return HttpResponseRedirect(reverse('idea_detail', args=[id]))

