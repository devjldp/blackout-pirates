from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Concert
from .forms import ConcertForm


# Create your views here.

def all_concerts(request):
    """
    A view to show all concerts
    Retrieves all concert records from the database and renders them in the concerts page.

    Args:
        request: The HTTP request object.
    """

    concerts = Concert.objects.all()

    context = {
        'concerts': concerts
    }
    return render(request, 'concerts/concerts.html', context)


def concert_detail(request, concert_id):
    """
    A view to show a concert detail.
    Retrieves a specific concert by its ID and renders the concert detail page.

    Args:
        request: The HTTP request object.
        concert_id: The ID of the concert to display.
    """

    concert = get_object_or_404(Concert, pk=concert_id)

    context = {
        'concert': concert
    }

    return render(request, 'concerts/concert_detail.html', context)

@login_required
def add_concert(request):
    """
    A view to add a new concert.

    Only accessible to superusers. Handles the form submission for adding a new concert.

    Args:
        request: The HTTP request object.
    """
    # Restrict access to superusers only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only admins can do that.')
        return redirect(reverse('home'))
    
    # Handle form submission for adding a new concert
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES)
        if form.is_valid():
            concert = form.save()
            messages.success(request, 'Successfully added concert!')
            return redirect(reverse('concert_detail', args=[concert.id]))
        else:
            messages.error(request, 'Failed to add concert. Please ensure the form is valid')
    else:
        # Initialize an empty form for adding a new concert
        form = ConcertForm()
    
    template= 'concerts/add_concert.html'
    context = {
        'form': form
    }
    
    print(context)
    return render(request, template, context)


@login_required
def edit_concert(request, concert_id):
    """
    A view to edit an existing concert.

    Only accessible to superusers. Handles the form submission for editing a concert.

    Args:
        request: The HTTP request object.
        concert_id: The ID of the concert to edit.
    """
    # Restrict access to superusers only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only admins can do that.')
        return redirect(reverse('home'))
    
    concert = get_object_or_404(Concert, pk = concert_id)
    
    # Handle form submission for editing the concert
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES, instance = concert)
        if form.is_valid():
            form.save()
            messages.success(request, ' Successfully updated product!')
            return redirect(reverse('concert_detail', args=[concert.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ConcertForm(instance=concert)
        messages.info(request, f'You are editing the concert for {concert.city}')
    
    # Define the template and context for rendering the edit concert page
    template = 'concerts/edit_concert.html'
    context = {
        'form': form,
        'concert': concert
    }
    
    return render(request, template, context)


@login_required
def delete_concert(request, concert_id):
    """
    A view to delete an existing concert.

    Only accessible to superusers. Deletes the specified concert from the database.

    Args:
        request: The HTTP request object.
        concert_id: The ID of the concert to delete.

    """
    # Restrict access to superusers only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only admins can do that.')
        return redirect(reverse('home'))
    
    concert = get_object_or_404(Concert, pk = concert_id)
    concert.delete()
    messages.success(request, 'Concert deleted!')
    # Redirect to the concerts page after deletion
    return redirect(reverse('concerts'))