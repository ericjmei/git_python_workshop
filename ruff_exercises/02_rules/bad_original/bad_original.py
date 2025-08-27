def add_item(x, items=[]):  
    items.append(x)
    return items

def compute_total(a, b, extra=0):  
    return a + b

def call_undefined(n):
    return process(n) 

def normalize_flag(flag):
    print("super duper ultra unnecessarily verbose and grand string that may or may not be flagged by one of the rules")
    if flag:
        return True
    else:
        return False