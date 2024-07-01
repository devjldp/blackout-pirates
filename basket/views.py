from django.shortcuts import render, redirect, reverse, HttpResponse

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
    # print(request.session['basket'])
    return redirect(redirect_url)


def update_basket(request, concert_id):

    quantity = int(request.POST.get('quantity'))
    print("Quantity:", quantity)

    basket = request.session.get('basket', {})
    print("basket:", basket)

    if quantity > 0:
        print(basket[concert_id])
        basket[concert_id] = quantity
    else:
        basket.pop(concert_id)

    print("basket updated", basket)
    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(reverse('view_basket'))
