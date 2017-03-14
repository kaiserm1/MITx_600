import math

def polysum(n, s):
    """
    input: integer n is the number of sides
           integer or float s is the length of a side
           in a regular polygon
           
    Sum the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    """
    
    perimeter = n * float(s)
    area = (0.25 * n * s**2)/(math.tan(math.pi/n))
    
    # return sum of perimeter squared and area, rounded to 4 decimal places.
    return round(perimeter**2 + area, 4)
