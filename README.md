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
def matches_email_regex(value):
    match_object = search(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
                          value)
    return bool(match_object)

is_valid_gmail = [
    "len(value) > 5",
    "'@' in value",
    matches_email_regex,
    "'gmail.com' in value"
]

my_email = "jeff.gruenbaum@gmail.com"

if ifandstatement(my_email, *is_valid_gmail):
    print("The email is valid!")
```
Output:
```The email is valid!```