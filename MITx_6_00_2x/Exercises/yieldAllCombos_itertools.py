from itertools import chain, combinations, filterfalse

def yieldAllCombos_itertooly(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # Generate powerset for bag 1 and bag 2.
    # Item in bag 1 == 1, item in bag 2 == 2. For each of the N items.
    bag1 = chain.from_iterable(combinations(items, r) for r in range(N))
    bag2 = chain.from_iterable(combinations(items, r) for r in range(N))
    yield (bag1, bag2)

'''    N = len(items)
    # Enumerate the 3**N possible combinations    
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
'''
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



an_iterable = [1, 2, 3, 4, 5, 6, 7, 8]
#r = [x for x in yieldAllCombos_itertooly(an_iterable)]
#print(r)
print(list(powerset(an_iterable)))
