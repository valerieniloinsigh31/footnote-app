from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings


from writer_profile.models import WriterProfile
from footnote.models import FootNote, Idea
from .models import Medley



# def medley(request):
#    """
#    view to render the Medley Page
#    """
#    template = 'medley.html'
#    return render(request, template)

# class MedleyList(generic.ListView):
#    model = 'Medley'
#    template_name = 'medley.html'

@login_required # consider deleting this so any user can view medley (anonymous)
# def medley(request):
#    """
#    view handling medley 
#    """
#    medley = get_object_or_404(Medley)
#    footnotes = FootNote.objects.all()  
#    template = 'medley.html'
#    context = {

#        'footnotes': footnotes,
#        'medley': medley,
#        'on_medley_page': True

#    }
#    return render(request, template, context)

def medley(request):
    """
    view to render the landing page
    """
    template = 'medley.html'
    return render(request, template)