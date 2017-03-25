def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # Convert int to str so we can access each digit.
    us_num_string = str(us_num)
    if us_num == 0:
        return trans['0']
    # If the number is single digit, just return the value for single digit.
    elif len(us_num_string) < 2:
        return trans[us_num_string]
    # If the number has a trailing 0, return translation without 0 at the end, 
    # else, return translation for all digits.
    else:
        if us_num_string == '10':
            return trans['10']
        if us_num_string[0] == '1':
            return trans['10'] + " " + trans[us_num_string[1]]
        return_string = trans[us_num_string[0]] + " " + trans['10']
        if us_num_string[1] == '0':
            return return_string
        else:
            return return_string + " " + trans[us_num_string[1]]
