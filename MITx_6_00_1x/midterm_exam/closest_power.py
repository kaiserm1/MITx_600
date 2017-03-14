def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    assert type(base) == int and base > 1, "'base' is not an integer and/or not > 1."
    assert type(int(num)) == int and num > 0, "'num' is not an integer and/or not > 0."
    if num <= 1:
        return 0
    else:
        exp = 1
        while True:
            if base**(exp-1) < num and base**exp > num:
                if num - base**(exp-1) <= base**exp - num:
                    return exp - 1
                else:
                    return exp
            elif base**exp == num:
                return exp
            else:
                exp += 1