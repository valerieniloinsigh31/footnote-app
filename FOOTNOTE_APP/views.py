from django.shortcuts import render
from django.http import Http404


def FOOTNOTE_APP(request):
    """
    view to render the landing page
    """
    template = 'index.html'
    return render(request, template)