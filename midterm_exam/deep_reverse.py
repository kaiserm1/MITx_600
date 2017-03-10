def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    assert type(L) == list, "L is not a list."
    assert type(L[0]) == list, "L is not a list of lists."
    new_L = []
    while L != []:
        helper_list = L.pop()
        new_L_helper = []
        while helper_list != []:
            new_L_helper.append(helper_list.pop())
        new_L.append(new_L_helper)
    for lists in new_L:
        L.append(lists)
    return L
