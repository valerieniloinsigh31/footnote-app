from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings


from writer_profile.models import WriterProfile
from footnote.models import FootNote, Idea
from .models import Medley
from django.views import generic, View

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import random
from footnote.forms import FootNoteForm


def medley(request):
    """
    view to render the landing page and generate random footnote
    """
    template = 'medley.html'
    random_footnote = FootNote.objects.order_by('?').first
    context = {
        'random_footnote': random_footnote, }
    return render(request, template, context)
