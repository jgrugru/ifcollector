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
is_valid_test_str = [
    str.isalnum,
    "value == 'Testing'",
    lambda value: value == 'Testing',
]

my_str = 'Testing'
print(ifandstatement(my_str, *is_valid_test_str))
```
Output:
```True```