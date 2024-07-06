from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_basket(request):
    """
      A view to return the basket page.
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, concert_id):
    """
    Add a quantity of a specific concert to the shopping basket.

    This view handles adding a specified quantity of a concert to the user's basket.
    If the concert is already in the basket, the quantity is updated.
    Otherwise, the concert is added with the specified quantity.

    Args:
        request: The HTTP request object containing POST data with 'quantity' and 'redirect_url'.
        concert_id: The ID of the concert to add to the basket.
    """
    
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
    """
    Update the quantity of a specific concert in the shopping basket.

    This view handles updating the quantity of a concert in the user's basket.
    If the new quantity is greater than 0, the concert's quantity is updated.
    If the new quantity is 0, the concert is removed from the basket.

    Args:
        request: The HTTP request object containing POST data with 'quantity'.
        concert_id: The ID of the concert to update in the basket.
    """
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
