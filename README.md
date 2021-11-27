# ifcollector
A better alternative to the any() and all() built-in python functions.

# Install
```python
pip install ifcollector
```

# How to

Ifcollector allows you to smartly evaluate a list of functions/expressions againt a single value.

Here is an example of how you would want to validate an inputted list:
```python
from ifcollector import ifandstatement

def do_digits_add_up_to_10(list_of_digits):
    total = 0
    for n in list_of_digits:
        total += n

    return bool(total == 10)

def are_all_values_digits(list_of_digits):
    for n in list_of_digits:
        if not isinstance(n, (int, float)):
            return False
    return True

# list of checks against the inputted list
is_list_valid_input = [
    "len(value) < 6",
    do_digits_add_up_to_10,
    are_all_values_digits,
    ]

inputted_list1 = [1,2,3,4,5,6,7]
inputted_list2 = [1,2,1,3,1,1,1]

if ifandstatement(inputted_list1, *is_list_valid_input):
    print("The inputted_list1 is valid!")

if ifandstatement(inputted_list2, *is_list_valid_input):
    print("The inputted_list2 is valid!")
```
Output:
```The inputted_list2 is valid!```

The expressions to evaluate against the value (the inputted_list) can be passed in an unpacked list or as individual expressions. AKA they can only be passed as individual expressions:

```ifandstatement(inputted_list, *is_list_valid_input)```

is equivalent to 

```ifandstatement(inputted_list, "len(value) < 6", do_digits_add_up_to_10, are_all_values_digits)```

The conditionals that will be evaluated against a single value can be a function,
a boolean expression in the form of a string, or a lambda. For all boolean expressions and lamdas,
the keyword __value__ will be used for the variable being evaluated.

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

### Please Note:
> If passing the boolean expressions in a list, you will need to use the [unpacking operator](https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/).

# Types of If Statements:
### [ifandstatement](https://github.com/jgrugru/ifcollector/blob/main/ifcollector/if_functions.py#L1)(value, boolean_expressions*)
- Aggregates the boolean expressions with an _and_ operator.
- Import into your python file with this statement:```from ifcollector import ifandstatement```.
### [iforstatement](https://github.com/jgrugru/ifcollector/blob/main/ifcollector/if_functions.py#L13)(value, boolean_expressions*)
- Aggregates the boolean expressions with an _or_ operator.
- Import into your python file with this statement:```from ifcollector import iforstatement```.

