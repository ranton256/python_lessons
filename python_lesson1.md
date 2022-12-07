# Python Lesson One

## Python

Python is a popular programming language. It's also what we're writing our game in.
Python is relatively easy to learn as a beginner. We are using Python version 3.
Python version 2 is still popular as well, but the syntax(the way you write programs in it)
is not completely compatible.

## Editor

We use an editor to edit the source code for a programming language while programming.

We are using PyCharm, which is not just an editor, but also an
IDE, integrated development environment, which means it also does things like manage our
project files for us and launch the program when we want to run it. It can also do lots of
other neat things.

Be sure and check out the "Help" menu in PyCharm to learn more about what it can do.

One of the things our PyCharm IDE provides is a Python Console. Click "Python Console" near the bottom of a project
window to open it.

## Hello, world

It's a tradition to start learning a new programming language by

```python
print("Hello, World!")
```

## Comments

If you want to write some text in your code to describe it or give someone reading it a hint you can
put that in a comment.

In python, any line that starts with a pound sign, '#', is a comment.

```python
    # This text is a comment.
```

## Variables

Variables are holders or buckets for values with a name.  For example:

```python
    i = 3
```

In this, i is the name of the variable, and the value three is being placed in
the variable. Later if we say `i = 5` i will still be the same variable, but
it will contain a different value.

To put it another way, variables are holders for values.

Variables can be different kinds of values called types.

Python is a dynamically typed language.  A language which is dynamically typed has
variables which can accept any value or only certain types of values.  For example, in a
dynamically typed language one variable could hold an integer(same meaning as
in algebra, a number with no fractional or decimal part) or a floating point
value (the normal way of representing numbers with something to the right of
the decimal place), or a string (which is an ordered list of characters as in
letters, numbers, spaces, and punctuation).

## Integers

Integers can hold any positive or negative whole number.
They mean the same as in algebra class.

```python
    print(42)
```

## Strings

Strings hold text, like names, words, sentences. They can be split up, combined.

```python
    s = "Hi"
    print(s)
    s= "Bye"
    print(s)
```

## Floating Point Numbers

Python also supports floating point numbers which can have a part to the right of the decimal place.

```python
    print(3.14)
    print(.25)
```

## None

None is a special type in Python meaning there is no other type. It's the value a variable has if nothing
has assigned it one. There is only one value for a variable of type None, which is the single value None.

```python
    v = None
    print(v)
```

## If/else

You use if statements and else statements when you only want code to be run if some certain condition is true.

True or false conditions can also be stored in Boolean variables, which is a variable that can only
have one of the two values, True or False. (Note that they start with a capital letter).

```python
    b = True
    if b:
        print("b is true")
    else:
        print("b is false")
```

Try changing that code to say b = False. What happens then?

```python
    x = 10
    if x == 10:
        print("x is 10!")   # you see this
    x = 9
    if x == 10:
        print("x is still 10")  # but not this
```

## Loops

A loop is a way to make some code in a program run multiple times. You can control how many time it runs
based on different conditions.

A common way to write a loop in Python is with a range. This prints the numbers from 0 to 9 (not 10).

```python
    for x in range(10):
        print(x)
```

## Lists

A list is a type that's a lot like it sounds. It holds a sequence of values.
A single variable can point to a list, which can have values added or removed.

It's easy to loop over all the values in a list.

```python
    cats = ["Anna", "Confetti", "Wade"]
    for cat in cats:
        print(cat)
```

Note that lists don't have to contain values of only a single type.

## Dictionaries

A dictionary in python is a collection data structure which holds unordered values indexed by keys. These keys can be any Python value, but most often are strings.

You can access a Python dictionary by putting the key you want in brackets, like this:

```python
val = my_dict["mykeyval"]
# you can also use the get method.
val = my_dict.get("mykeyval")
```

You can also modify the value by referencing the key the same way on the left side of the equals.

```python
my_dict["mykeyval"] = 123;
```

And you can insert into the dictionary the same was as above. The assignment will either create or update an entry in the dictionary at the specified key.

You can create a dictionary with its contents by enclosing key value pairs with a colon between the key and value inside curly braces with each pair separated by a comma.

```python
my_dict = {
    "orange": "fruit",
    "apple": "fruit",
    "pea": "vegetable",
    "grape": "fruit",
    "squash": "vegetable" 
}
```

You can loop over all the keys in a dictionary with a for loop, similar to the values in a list.

```python
for key in my_dict:
    print("{} is {}".format(key, my_dict[key]))
```

You can delete(remove) a key-value entry from a dictionary using the `del` keyword.

```python
del my_dict["pea"]   # some people don't like peas :(
```

You can delete all the entries using `clear()`.

```python
my_dict.clear()  # I'm not even hungry.
```

You can loop over the keys and values more easily like this:

```python
for k, v in my_dict.items():
  print(k, v)
```

## Project

Make a list of everyone in your family, including pets, loop over them,
and print out their name, age and category (cat, dog, donkey, girl or boy, young, tween, teen, adult).

## References

* <https://realpython.com/python-data-types/>
* <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>
