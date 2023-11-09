def calculate_simple_interest_rate(principal, interest, time):
    simple_interest = principal * interest * time
    return simple_interest


def calculate_compound_interest_rate(principal, interest, times_compounded, time):
    compound_interest = principal * (1 + interest/times_compounded) ** (times_compounded * time) - principal
    return round(compound_interest, 2)