from django.shortcuts import render

# import a model from other app
from concerts.models import Concert


# Create your views here.

def index(request):
    """
      A view to return the index page
    """
    concerts = Concert.objects.all()

    return render(request, 'home/index.html', {"concerts": concerts})
