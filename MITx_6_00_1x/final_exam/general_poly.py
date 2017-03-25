def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def formula_generator(x):
        formula = 0
        k = len(L) - 1
        for n in range(len(L)):
            formula += L[n] * x ** k
            k -= 1
        return formula

    return formula_generator
