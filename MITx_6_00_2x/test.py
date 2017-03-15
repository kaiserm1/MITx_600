from itertools import takewhile
r = range(5)
print(list(takewhile(lambda x: x < 3, r)))

