def add_item(x, items=None): # rule B006, changed mutable struct to initialize in function
    if items is None:
        items = []
    items.append(x)
    return items

def compute_total(a, b):  # rule ARG001, removed argument extra
    return a + b

def call_undefined(n):
    def process(x): # rule F821, no "one" fix
        return x * 2 # arbitrary
    return process(n) 

def normalize_flag(flag):
    print("super duper ultra unnecessarily verbose and grand string" +
          " that may or may not be flagged by one of the rules") # rule E501, broke long line
    return flag # rule SIM103, return flag directly