from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings


from customer_profile.models import WriterProfile
from .forms import WriterProfileForm


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
    orders = writer_profile.orders.all()
    template = 'writer_profile/profile.html'
    context = {

        'form': form,
        'orders': orders,
        'customer_profile': customer_profile,
        'on_profile_page': True

    }
    return render(request, template, context)


def order_history(request, order_number):
    """
    render order history
    """

    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
