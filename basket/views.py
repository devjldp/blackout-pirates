from django.shortcuts import render, redirect

# Create your views here.


def view_basket(request):
    """
      A view to return the basket page.
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, concert_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if concert_id in list(basket.keys()):
        basket[concert_id] += quantity
    else:
        basket[concert_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
