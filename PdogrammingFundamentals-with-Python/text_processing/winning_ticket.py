tickets = [ticket.strip() for ticket in input().split(', ')]


def check_the_ticket(some_ticket):
    if len(some_ticket) != 20:
        return "invalid ticket"
    left_part = some_ticket[:10]
    right_part = some_ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    for symbol in winning_symbols:
        for count in range(10, 5, -1):
            winning_combination = count * symbol
            if winning_combination in left_part and winning_combination in right_part:
                message = f'ticket "{some_ticket}" - {count}{symbol}'
                if count == 10:
                    message += f' Jackpot!'
                return message
    return f'ticket "{some_ticket}" - no match'


for ticket in tickets:
    print(check_the_ticket(ticket))
