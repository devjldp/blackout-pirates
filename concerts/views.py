from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Concert
from .forms import ConcertForm


# Create your views here.

def all_concerts(request):
    """A view to show all concerts"""

    concerts = Concert.objects.all()

    context = {
        'concerts': concerts
    }
    return render(request, 'concerts/concerts.html', context)


def concert_detail(request, concert_id):
    """A view to show a concert detail"""

    concert = get_object_or_404(Concert, pk=concert_id)

    context = {
        'concert': concert
    }

    return render(request, 'concerts/concert_detail.html', context)

@login_required
def add_concert(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only admins can do that.')
        return redirect(reverse('home'))
    
    
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES)
        if form.is_valid():
            concert = form.save()
            messages.success(request, 'Successfully added concert!')
            return redirect(reverse('concert_detail', args=[concert.id]))
        else:
            messages.error(request, 'Failed to add concert. Please ensure the form is valid')
    else:
        form = ConcertForm()
    
    template= 'concerts/add_concert.html'
    context = {
        'form': form
    }
    
    print(context)
    return render(request, template, context)


@login_required
def edit_concert(request, concert_id):
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only admins can do that.')
        return redirect(reverse('home'))
    
    concert = get_object_or_404(Concert, pk = concert_id)
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
        
    template = 'concerts/edit_concert.html'
    context = {
        'form': form,
        'concert': concert
    }
    
    return render(request, template, context)


@login_required
def delete_concert(request, concert_id):
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only admins can do that.')
        return redirect(reverse('home'))
    
    concert = get_object_or_404(Concert, pk = concert_id)
    concert.delete()
    messages.success(request, 'Concert deleted!')
    return redirect(reverse('concerts'))