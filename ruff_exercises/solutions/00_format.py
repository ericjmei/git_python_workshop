import math, sys # why didn't this get fixed?


def foo(x: int = 1, y=2):
    """does stuff"""
    if x > 10:
        return x * y
    return x + y


long_str = "this is a really long string that probably should wrap or get split to respect line length limits and trailing whitespace" # why didn't this get fixed?

long_dict = {
    "key_0": "value_0",
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3",
    "key_4": "value_4",
}
