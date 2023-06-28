from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings


from writer_profile.models import WriterProfile
from footnote.models import FootNote, Idea
from .models import Medley

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import random
from footnote.forms import FootNoteForm

# def medley(request):
#    """
#    view to render the Medley Page
#    """
#    template = 'medley.html'
#    return render(request, template)

# class MedleyList(generic.ListView):
#    model = 'Medley'
#    template_name = 'medley.html'

# @login_required # consider deleting this so any user can view medley (anonymous)
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

def footnote_medley(request, content):
    """
    render footnote medley...try to use random function so one random footnote can be summoned from database
    """

    footnote = get_object_or_404(FootNote, content=content, user=request.user,)

    template = 'medley.html'
    context = {
        'footnote': footnote,
        'content': content,
        'from_footnote': True,
        'user': request.user,
    }

    return render(request, template, context)
  


def random_footnote(request):
    """
    generate random idea for medley 
    """
    footnote_ids= FootNote.objects.all().values_list('footnote_id',flat=True)
    random_obj = FootNote.objects.get(footnote_id=random.choice(list(footnote_ids)))
    context = {
    'random_obj':random_obj,}
    return render(request, 'medley/medley.html', context)