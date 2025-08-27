def add(a: int, b: int):
    """
    Add two integers. James!

    Parameters
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns
    -------
    int
        The sum of a and b.
    """
    return a + b

def subtract(a: int, b: int):
    """
    Subtract one integer from another. Iana!

    Parameters
    ----------
    a : int
        The integer to subtract from.
    b : int
        The integer to subtract.

    Returns
    -------
    int
        The difference between a and b.
    """
    return -1

def multiply(a: int, b: int):
    """
    Multiply two integers. Sydney!

    Parameters
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns
    -------
    int
        The product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide one number by another. Alex!

    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.

    Returns
    -------
    float
        The quotient of a divided by b.
    """
    return -1

def exponent(a: float, b: float):
    """
    Raise one number to the power of another. Eric!

    Parameters
    ----------
    a : float
        The base number.
    b : float
        The exponent number.

    Returns
    -------
    float
        The result of a raised to the power of b.
    """
    return a ** b

def mod(a: float, b: float):
    """
    Calculate the remainder when dividing `a` by `b`.

    Args:
        a : float
            The dividend.
        b : float
            The divisor.

    Returns:
    float
        The remainder after dividing `a` by `b`.
    """
    return -1

if __name__ == "__main__":

    start_num = 1

    temp_num = add(start_num, 2)
    temp_num = subtract(temp_num, 1)
    temp_num = multiply(temp_num, 6)
    temp_num = divide(temp_num, 3)
    temp_num = exponent(temp_num, 2)
    temp_num = mod(temp_num, 4)

    print(f"Final number: {temp_num}")
    print(f"Expected: 0.0")
