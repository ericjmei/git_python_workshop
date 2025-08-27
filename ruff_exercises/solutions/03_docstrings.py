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

# NOTE: ruff doesn't check for heading or table style — you need a different package for that (e.g., pydocstyle)
def bad_function(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int
        The sum of the two numbers.

    Examples
    --------
    >>> bad_function(2, 3)
    5
    """
    return a + b
