from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings


from writer_profile.models import WriterProfile
from .forms import WriterProfileForm
from footnote.models import FootNote


@login_required
def writerprofile(request):
    """
    view handling writer profile
    """
    writer_profile = get_object_or_404(WriterProfile, user=request.user)
    if request.method == 'POST':
        form = WriterProfileForm(request.POST, instance=writer_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your writer profile is updated")
        else:
            messages.error(request,
                           'Failed to update writer profile')
    else:
        form = WriterProfileForm(instance=writer_profile)

    footnotes = FootNote.objects.all()
    template = 'writer_profile/writerprofile.html'
    context = {

        'form': form,
        'footnotes': footnotes,
        'writer_profile': writer_profile,
        'on_writerprofile_page': True

    }
    return render(request, template, context)


def footnote_history(request, content, created_on, user):
    """
    render footnote history
    """

    footnote = get_object_or_404(FootNote, content=content,
                                 created_on=created_on,
                                 user=request.user,)
    messages.info(request, (
        f'Your footnote: {content} on the following date {created_on} '
    ))

    template = 'writer_profile/writerprofile.html'
    context = {
        'footnote': footnote,
        'content': content,
        'created_on': created_on,
        'from_footnote': True,
        'user': request.user,
    }

    return render(request, template, context)


@login_required
def delete_footnote(request, footnote_id, *args, **kwargs):

    footnote = get_object_or_404(WriterProfile, id=footnote_id)
    footnote.delete()
    return redirect(request, 'writerprofile')
