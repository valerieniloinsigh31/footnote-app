from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings


from customer_profile.models import WriterProfile
from .forms import WriterProfileForm
from footnote.models import FootNote


@login_required
def profile(request):
    """
    view handling writer profile
    """
    writer_profile = get_object_or_404(WriterProfile, user=request.user)
    if request.method == 'POST':
        form = WriterProfileForm(request.POST, instance=writer_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile is updated")
        else:
            messages.error(
                  request,
                  'Failed to update profile please check your form for errors')
    else:
        form = WriterProfileForm(instance=writer_profile)
    footnotes = writer_profile.footnotes.all()
    template = 'writer_profile/writerprofile.html'
    context = {

        'form': form,
        'footnotes': footnotes,
        'writer_profile': writer_profile,
        'on_writerprofile_page': True

    }
    return render(request, template, context)


def footnote_history(request, footnote_content):
    """
    render footnote history
    """

    footnote = get_object_or_404(FootNote, footnote_content=footnote_content)
    messages.info(request, (
        f'You posted the following footnote: {footnote_content}. '
    ))

    template = 'footnote/footnote.html'
    context = {
        'footnote': footnote,
        'from_writerprofile': True,
    }

    return render(request, template, context)
