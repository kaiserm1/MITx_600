def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # tuple with 2 dicts. 1st is intersect, 2nd is difference

    helper_dict_inter = {}
    helper_dict_diff = {}
    
    for key in d1.keys():
        if key in d2.keys():
            helper_dict_inter[key] = f(d1[key], d2[key])
    
    for key in d2.keys():
        if key not in d1.keys():
            helper_dict_diff[key] = d2[key]
    for key in d1.keys():
        if key not in d2.keys():
            helper_dict_diff[key] = d1[key]
    return (helper_dict_inter, helper_dict_diff)