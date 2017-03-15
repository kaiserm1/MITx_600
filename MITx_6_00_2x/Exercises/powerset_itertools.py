from itertools import chain, combinations

def powerset(items):
    """
        Generates all combinations of N items.
        Items is an iterable.

        Yields a list of tuples for all possible combinations of items.
    """
    return chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))