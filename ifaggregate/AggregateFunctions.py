
def ifandstatement(value, *args, debug=False):
    if debug:
        print("ifandstatement(value=" + value + ")")
    result = True
    for expression in args:
        if result:
            if isinstance(expression, str):
                result = eval(expression, {}, {'value': value})
                if debug:
                    print(expression, result)
            else:
                result = expression(value)
                if debug:
                    print(expression.__name__, result)
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
    contains_at,
    "value == 'IamastTring'",
]

print(ifandstatement("IamastTring", *is_valid, debug=True))