"""
Zydelo - June 21, 2021
"""

def power(base, exponent):
    # Base Case
    if exponent == 0 :
        return 1

    # Recursive Case
    else :
        return base * power(base, exponent - 1)
# Driver Code
print(power(2, 3))

