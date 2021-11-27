from dataclasses import dataclass
from typing import Union, Callable
from ifcollector.exceptions import CannotEvaluateExpression


@dataclass
class ExpressionEvaluator:
    expression: Union[str, Callable]
    value: object
    debug: bool

    def parse_expression(self) -> bool:
        if isinstance(self.expression, str):
            result = self.evaluate_str()
        elif isinstance(self.expression, Callable):
            result = self.evaluate_fn()
        else:
            raise TypeError
        return result

    def evaluate_str(self) -> bool:
        try:
            # pass value as a local var
            result = eval(self.expression, {}, {"value": self.value})
            if self.debug:
                print(self.expression, "-->", result)
        except Exception:
            print(f"{self.expression} is not callable on {self.value}")
            raise CannotEvaluateExpression
        return result

    def evaluate_fn(self) -> bool:
        try:
            result = self.expression(self.value)
            if self.debug:
                print(self.expression.__name__, "-->", result)
        except Exception:
            print(f"{self.expression} is not callable on {self.value}")
            raise CannotEvaluateExpression
        return result
