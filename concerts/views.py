from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

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


def add_concert(request):
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added concert!')
            return redirect(reverse('add_concert'))
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



def edit_concert(request, concert_id):
    
    concert = get_object_or_404(Concert, pk = concert_id)
    form = ConcertForm(instance=concert)
    
    messages.info(request, f'You are editing {concert.city}')
    
    template = 'concerts/edit_concert.html'
    context = {
        'form': form,
        'concert': concert
    }
    
    return render(request, template, context)