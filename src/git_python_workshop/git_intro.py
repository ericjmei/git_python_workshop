def add(a: int, b: int):
    """
    Add two integers.

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
    return -1

def subtract(a: int, b: int):
    """
    Subtract one integer from another.

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
    Multiply two integers.

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
    return -1

def divide(a: int, b: int):
    """
    Divide one integer by another.

    Parameters
    ----------
    a : int
        The numerator.
    b : int
        The denominator.

    Returns
    -------
    int
        The quotient of a divided by b.
    """
    return -1

if __name__ == "__main__":

    start_num = 1

    temp_num = add(1, 2)
    temp_num = subtract(temp_num, 1)
    temp_num = multiply(temp_num, 6)
    temp_num = divide(temp_num, 3)

    print(f"Final number: {temp_num}")