from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Idea, FootNote
from .forms import FootNoteForm
from django.views.generic import ListView

class AddIdea(View):
    model = Idea
    template_name = 'add_idea.html'
    fields = '__all__'
    #exclude = [‘slug’,] 

    def post(self, request):
        if request.method == 'POST':
           idea = Idea.objects.create()
           idea_form = IdeaForm(data=request.POST)
           idea.save()
        else:
            if idea_form.is_valid():
                idea_form.instance.email = request.user.email 
                idea_form.instance.name = request.user.username
                idea = idea_form.save(commit=False)
                idea.idea = idea
                idea.save()
            else:
                idea_form = IdeaForm()
        return redirect('')
        return render(request, self.template_name,
        {
                "idea_form": IdeaForm()
            },)


class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 3

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

#class AddIdea(View):
#    model = Idea
#    template_name = 'add_idea.html'
#    fields = '__all__'
    #exclude = [‘slug’,] 

#    def post(self, request):
#        if request.method == 'POST':
#           idea = Idea.objects.create()
#           return redirect('')
#        return render(request, self.template_name)
    #model = Idea
    #template_name = 'add_idea.html'
    #fields = '__all_'

    #def add_item(request):
    #    if request.method == 'POST':
    #        Idea.objects.create
    #        return redirect('idea_detail')
    #    return render(request, 'footnote/add_idea/html')

class IdeaLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Idea, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('idea_detail', args=[slug]))

class IdeaEdit(View):

    def post(self, request, slug):
        post = get_object_or_404(Idea, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('idea_detail', args=[slug]))

class IdeaDelete(View): #DON'T THINK A SEPARATE FUNCTION NEEDS TO BE CREATED FOR DELETION

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

