import os
import sys, json

from pathlib import Path
import numpy as np  


def main():
    """goal: print 'done! result: 3'"""
    data = json.loads('{"a": 1}')
    path = Path("somewhere")
    b = 2
    result = compute(a, b)
    unused = 42
    print(f"done! result: {result}")
    return result


def compute(a, b, c=0):
    return a + b

if __name__ == "__main__":
    main()