def sqrt(x):
    '''Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.

    Returns:
        The square root of x.
    '''
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print("Cannot compute square of negative number.")
    
    print("Program continues normally.")

if __name__ == '__main__':
    main()


def sqrt2(x):
    '''Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.

    Returns:
        The square root of x.
    
    Raises:
        ValueError: If x is negative.
    '''
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

try:
    print(sqrt2(9))
    print(sqrt2(-1))
    print("this line never reached.")
except ValueError as e:
    print(e)

print("Program continues normally.")

