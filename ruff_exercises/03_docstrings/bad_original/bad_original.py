def good_function(x, y):
    """
    Add two numbers.

    Parameters
    ----------
    x : int
        The first number.
    y : int
        The second number.

    Returns
    -------
    int
        The sum of the two numbers.

    Notes
    -----
    This is just an example of a well-written docstring.

    Examples
    --------
    >>> good_function(2, 3)
    5
    """
    return x + y


def bad_function(a, b):
    """adds two numbers but docstring is messy
    parameters a b just numbers 
    returns something idk
    Example:
        >>> def foo(x,y):return x+y   # inline code, not valid example
    also the first line doesnt end properly
    """
    return a + b
