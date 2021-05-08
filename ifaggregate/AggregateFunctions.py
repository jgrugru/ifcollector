def ifandstatement(value, *args, debug=False):
    if debug:
        print("ifandstatement(value=" + value + ", args=" + str(args) + ")")
        print("------------------------------")
    result = True
    for expression in args:
        if result:
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
