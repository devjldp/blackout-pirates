from django.conf import settings
from django.shortcuts import get_object_or_404
from concerts.models import Concert



def basket_contents(request):
    basket_tickets = []
    total = 0
    tickets_count = 0

    basket = request.session.get('basket', {} )

    for concert_id, quantity in basket.items():
        concert = get_object_or_404(Concert, pk = concert_id)
        total += quantity*500 # Sustituir por concert.price
        tickets_count += quantity
        basket_tickets.append({
            'concert_id': concert_id,
            'quantity': quantity,
            'city': concert
        })
    grand_total = total
    context = {
        "basket_tickets": basket_tickets,
        "total": total,
        "tickets_count": tickets_count,
        "grand_total": grand_total
    }

    return context
