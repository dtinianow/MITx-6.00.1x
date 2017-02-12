def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    closest_power = 0

    while base ** closest_power < num:
        closest_power += 1

    current_value = base ** (closest_power - 1)
    next_value = base ** (closest_power)

    if (abs(next_value - num)) < (abs(current_value - num)):
        return closest_power
        
    return closest_power - 1
