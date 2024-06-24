

def basket_contents(request):
    basket_tickets = []
    total = 0
    tickets_count = 0

    grand_total = total
    context = {
        "basket_tickets": basket_tickets,
        "total": total,
        "tickets_count": tickets_count,
        "grand_total": grand_total
    }

    return context
