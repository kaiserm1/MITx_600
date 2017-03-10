def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # tuple with 2 dicts. 1st is intersect, 2nd is difference
    result = ()
    helper_dict_inter = {}
    helper_dict_diff = {}
    
    for key in d1.keys():
        if d2.get(key):
            helper_dict_inter[key] = d1[key]
    # intersect
    for key in d1.keys():
        if d2.get(key):
            print(d1[key], d2[key])
            
    # difference
    for key in d1.keys():
        if not d2.get(key):
            print(d1[key])
    for key in d2.keys():
        if not d1.get(key):
            print(d2[key])