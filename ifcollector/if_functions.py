from ifcollector.expression_evaluator import ExpressionEvaluator


def ifandstatement(value: object, *args, debug: bool = False) -> bool:
    if debug:
        print_debug_intro("ifandstatement", value, args)

    result = True
    for expression in args:
        evaluatee = ExpressionEvaluator(expression, value, debug)
        if result:
            result = evaluatee.parse_expression()
        else:
            break
    return result


def iforstatement(value: object, *args, debug: bool = False) -> bool:
    if debug:
        print_debug_intro("iforstatement", value, args)

    result = False
    for expression in args:
        evaluatee = ExpressionEvaluator(expression, value, debug)
        if not result:
            result = evaluatee.parse_expression()
        else:
            break
    return result


def print_debug_intro(function_name, value, *args) -> None:
    print(function_name + "(value=" + str(value) + ", args=" + str(args) + ")")
    print("------------------------------")
