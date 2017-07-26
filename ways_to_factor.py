# Have to order factors from smallest to largest
# Factors must be unique

def bad_factor(x):
    factors = []
    for i in range(1, x):
        if (x % i == 0):
            factors.append(i)
    factors.append(x)
    return factors

def tests():
    print(bad_factor(100))
