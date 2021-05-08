
def ifandstatement(value, *args, debug=False):
    if debug:
        print("ifandstatement(value=" + value + ")")
    result = True
    for fn in args:
        if result:
            result = fn(value)
            if debug:
                print(fn.__name__, result)
        else:
            break
    return result

def is_str(value):
    if isinstance(value, str):
        return True
    else:
        return False


def contains_at(value):
    if 'T' in value:
        return True
    else:
        return False

is_valid = [
    str.isalnum,
    is_str,
    contains_at
]

print(ifandstatement("IamastTring", *is_valid, debug=True))