def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    assert len(listA) == len(listB), "Lists do not have the same length."
    list_result = []
    for i in range(len(listA)):
        assert type(listA[i]) == int and type(listB[i]) == int, "List values are not integers."
        list_result.append(listA[i] * listB[i])
    return sum(list_result)