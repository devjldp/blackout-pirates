from django.shortcuts import render

from .models import Concert


# Create your views here.

def all_concerts(request):
  """A view to show all concerts"""
  
  concerts = Concert.objects.all()
  
  context = {
    'concerts': concerts
  }
  return render(request, 'concerts/concerts.html', context)