from django.shortcuts import render

# import a model from other app
from concerts.models import Concert


# Create your views here.

def index(request):
    """
      A view to return the index page.
      This view fetches all Concert objects from the database
    and renders the 'home/index.html' template, passing the
    concerts as context data.
    """
    concerts = Concert.objects.all()
    return render(request, 'home/index.html', {"concerts": concerts})
