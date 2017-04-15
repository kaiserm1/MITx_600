def greedySum(L, s):
    """
    Use the greedy approach where you find the largest multiplier for
    the largest value in L then for the second largest, and so on to
    solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
    :param L: list of unique positive integers sorted in descending order
    :param s: positive integer, what the sum should add up to
    :return: the sum of the multipliers or "no solution" if greedy
             approach does not yield a set of multipliers such that the
             equation sums to 's'.
    """
    multipliers = []
    for  i in L:
        multipliers.append(s//i)
        s -= i * (s//i)
        if s == 0:
            return sum(multipliers)
    return "no solution"

print(greedySum([10, 4, 3, 1], 138))