from django.conf import settings
from django.shortcuts import get_object_or_404
from concerts.models import Concert


def basket_contents(request):
    basket_tickets = []
    total = 0
    tickets_count = 0

    basket = request.session.get('basket', {})

    for concert_id, quantity in basket.items():
        # get the concert using the primary key
        concert = get_object_or_404(Concert, pk=concert_id)
        total += quantity*concert.price  # Sustituir por concert.price
        subtotal = quantity * concert.price
        tickets_count += quantity
        basket_tickets.append({
            'concert_id': concert_id,
            'quantity': quantity,
            'city': concert.city,
            'price': concert.price,
            'subtotal': subtotal
        })
    grand_total = total
    context = {
        "basket_tickets": basket_tickets,
        "total": total,
        "tickets_count": tickets_count,
        "grand_total": grand_total
    }

    return context
