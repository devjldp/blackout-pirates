from django.shortcuts import render, get_object_or_404

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
    form = ConcertForm()
    template= 'products/add_product'
    context = {
        'form': form
    }
    
    return render(request, template, context)