from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
# Create your views here.


@login_required
def profile(request):
    """
    Display the user's profile and handle profile updates.

    If the request method is POST, update the user profile with the submitted data.
    If the request method is GET, display the profile form with the current profile data.

    Args:
        request: The HTTP request object.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # Handle form submission for profile updates
    if request.method == 'POST':
        form = UserProfileForm( request.POST, instance = profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Updated failed. Please ensure the form is vallid.')
            
    # print(profile)
    else:
        # Initialize the form with the current profile data
        form = UserProfileForm(instance=profile)
    
    # Retrieve all orders associated with the user profile
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    # print(orders)
    return render(request, template, context)


def order_history(request, order_number):
    """
    Display the order history for a specific order.

    Args:
        request: The HTTP request object.
        order_number: The order number of the order to display.
    """
    
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # Define the template and context for rendering the order confirmation page
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)