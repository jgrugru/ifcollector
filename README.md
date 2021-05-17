# ifcollector
A framework for creating complex if statements.

```python
pip3 install ifcollector
```

# How to

With ifcollector, if statements can be created from lists. For complex if statements,
stating all your conditionals in a list has the advantage of making code more
readable and reuseable.

To use it, create a list with all the conditionals that will be evaluated against a single value.
The conditionals can be a function, a boolean expression in the form of a string, or a lambda.
For all boolean expressions and lamdas, the keyword __value__ will be used for the variable being
evaluated.

```python
from ifcollector import ifandstatement

def add_digits(n):
    sum = 0
    for digit in str(n):
        sum += abs(int(digit))
    return sum

def do_digits_add_up_to_10(n):
    return add_digits(n) == 10

is_valid_input = [
    "value in range(0, 100)",
    do_digits_add_up_to_10,
    lambda value: int(str(value)[0]) % 2 == 1  # is the first digit odd?
]

if ifandstatement(73, *is_valid_input):
    print("The input is valid!")
```
Output:
```The input is valid!```

# Types of If Statements:
### [ifandstatement](https://github.com/jgrugru/ifcollector/blob/main/ifcollector/if_functions.py#L1)(value, boolean_expressions)
- Aggregates the boolean expressions with an _and_ operator.
### [iforstatement](https://github.com/jgrugru/ifcollector/blob/main/ifcollector/if_functions.py#L13)(value, boolean_expressions)
- Aggregates the boolean expressions with an _or_ operator.
