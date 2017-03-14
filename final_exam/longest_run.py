def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    start = 0
    end = 0
    max_length = 0
    for i in range(len(L) + 1):
        for j in range(i, len(L) + 1):
            if L[i:j] == sorted(L[i:j]):
                if len(L[i:j]) > max_length:
                    max_length = len(L[i:j])
                    start = i
                    end = j
            elif L[i:j] == sorted(L[i:j], reverse = True):
                if len(L[i:j]) > max_length:
                    max_length = len(L[i:j])
                    start = i
                    end = j
    return sum(L[start:end])
