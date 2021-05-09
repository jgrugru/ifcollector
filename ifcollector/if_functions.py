def ifandstatement(value, *args, debug=False):
    if debug:
        debug_intro("ifandstatement", value, args)
    result = True
    for expression in args:
        if result:
            result = parse_expression(expression, value, debug)
        else:
            break
    return result


def iforstatement(value, *args, debug=False):
    if debug:
        debug_intro("iforstatement", value, args)
    result = False
    for expression in args:
        if not result:
            result = parse_expression(expression, value, debug)
        else:
            break
    return result


def parse_expression(expression, value, debug):
    if isinstance(expression, str):
        result = eval(expression,
                      {},
                      {'value': value})  # pass value as a local var
        if debug:
            print(expression, "-->", result)
    else:
        result = expression(value)
        if debug:
            print(expression.__name__, "-->", result)
    return result


def debug_intro(function_name, value, *args):
    print(function_name + "(value=" + str(value) + ", args=" + str(args) + ")")
    print("------------------------------")
