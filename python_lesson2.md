# Python Lesson Two

## Functions

Functions are a separate unit of code execution in Python and many other programming languages.

They let you define code that can be reused with different inputs called parameters as often as you like without repeating the code itself.

```python
def say_hi(name):
    print("Hello,", name)

say_hi("Joe") # this is a function call
say_hi("Anne")
# Can you guess what this will print?
```

If you run this in your Python console inside PyCharm or by starting up Python on the command line, then you'll see this:

> Hello, Joe
> Hello, Anne

Functions can also return a value, using a return statement. The value is whatever the function wants to send back to its caller, and can depend on what the inputs are.

```python
def take_two(x):
    print("You gave me ", x)
    result = x - 2
    print("I am keeping two and giving back", result)
    return result

print("I got back", take_two(7))
print("I got back", take_two(5))
```

If you run this code you should see:

> You gave me  7
> I am keeping two and giving back 5
> I got back 5
> You gave me  5
> I am keeping two and giving back 3
> I got back 3

## Modules

You can import code from other files in Python using modules.

A module is an object that holds Python code, and can be used as a way to organize code.

You can import an entire module or just part of it.

### Imports

You use the "import" keyword to import modules into your own Python module's code to use it.

There are Python module search paths that will let you find modules by name in the system paths, or you can refer to them by a relative path name.

To import the pygame module, you would use a statement like this:

```python
import pygame
```

If you add a "levels.py" file in the same directory as your source file you could import it like this:

```python
import levels
```

You can also import specific things from a module using from <Module> import <thing>. You could import the randint function from the random module like this.

```python
from random import randint
```

When you import something like this you don't have to quality it with the module name; you can just call randint() like this.

```python
if randint(0, 1) == 0:
 enemies[a].image = "batframe1"
```

But if you imported it like so, you'd have to use <modulename>.<thing> to use code from the module.

```python
import random

if random.randint(0, 1) == 0:
 enemies[a].image = "batframe1"
```

## Console I/O

I/O stands for input/output. The console is the text screen you print text to and type into when running a Python program.

Use `print()` to send text to the console like we have already done.

To get text from the user you use `input()`. The input function takes an argument for a prompt string to print, then reads a string of user input. If the end of file (yes the console can have end of file) is reached, then a EOFError is raised; see the Exceptions section to see how to handle that.

```python
s = input('Enter your name: ')  
print("You entered", s)
```

## Formatting Strings

In order to build strings up with variable values substituted in them and print things exactly as you please, it's very useful to use the format() method of string objects in Python. This was added in Python3 but then also added to Python 2.

```python
"The sum of 1 + 2 is {0}".format(1+2)  # --> 'The sum of 1 + 2 is 3'
```

If you leave out the position (the 0 in the string above) then it defaults to in the same order as the arguments.

```python
"This is {} and this is {}".format("first", "second")   # --> 'This is first and this is second'
```

## Files

Files are the main unit of storing and organizing data into long-term storage on computers, such as hard disks and solid state disks.  Disks are split into partitions. Each partition is formatted into a filesystem volume.  A modern filesystem supports dividing the volume into folders (also called directories). A file is a series of bytes stored in a directory in a volume. Directories can also contain other directories within them.

The path of a file is a sequence of folder names followed by a filename specifying where the file is on disk.

In some operating systems, like Windows, the volume is part of the pathname before the directory names. In other filesystems, like Linux and Mac OS X, a volume is just mounted at a particular directory called a mountpoint which could be anywhere in the filesystem, with one filesystem known as root, and represented by a '/' usually as the beginning of the path. A path could point to a directory or a file (and other kinds of things on some systems).

For example,

`C:\Users\ranto\pyinstall_test` is a directory path on Windows on the C volume, which is the normal name for the main volume on windows.

`/home/ranton/sketchbook/libraries/readme.txt` is a file path on my Linux workstation.

## File I/O

File I/O means reading from and writing to files.

To open a file means to prepare it for reading or writing and get an object or reference for doing so, called a file object, file descriptor, or file handle. In python we use the `open()` function to open a file and get a file object in return which we can use to do things to the file.

```python
f = open('myfilespath', 'r')  # open a file for read (the 'r')
```

When you open a file, the second argument is the file mode.

* 'r' read only
* 'w' write only, replaces existing contents of file if it already exists.
* 'a' open file for appending, writes will get at added to end of current contents
* 'r+' open for reading and writing.
* not passing the mode argument defaults to mode of 'r'

When you are done with a file object you must close it.

```python
f.close()
```

You can use the `with`keyword to make sure files get closed automatically. Your object file will be available inside the with block, but closed automatically when you leave the with block.

```python
with open('myfilespath', 'r')  as f:
 read_data = f.read()
# file is closed now.
```

To get something from the contents of a file, you use read, and to put something in the contents of a file you use write. In the example above read_data contains everything in the file.

`f.readline()` reads one line of text from the file. A line means everything until the next newline character, a '\n', or the end of the file. If a newline was read it's included in the string returned.

You can also treat a file like it's a sequence or range and use it in a for loop to get the lines from it each time through the loop like this.

```python
for line in f:
 print(line)
```

`f.write(string)` writes the characters in *string* to the file object and returns the number of characters written.

A file object has a current position which you can change using `f.seek(newposition)`.

You can find out the current position of the file object by calling `f.tell()`

Normally files are text mode, by default, when you call open. You can open a file in binary mode instead by passing a 'b' character as part of the mode argument to open.

```python
f = open('workfile', 'rb+')
```

Python has special file objects sys.stdin and sys.stdout and sys.stderr for using file I/O with the console input and output.

You can use print() to a file destination as well. By default it prints (writes) to sys.stdout.

```python
print("to a file", file=f)
```

## Exceptions

If you try to open a file that does not exist for reading or a file you do not have permissions to access you will get an exception. An exception is a kind of error. Exceptions are triggered by the raise keyword in python and have to be caught and handled or the program will exit by default.

We will not go too far into handling exceptions right now, but here is how you would handle file open errors.

```python
import sys

try:
    with open('somefile/path.txt') as f:
     s = f.readline()
except OSError as err:
    # print out the error we had from open
    print("OS error: {0}".format(err))
except:
    # we don't know how to handle ths, so print it out and raise it again.
    # if nothing above us on call stack catches it, we will exit the program
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

If you run that code, you will see this unless you really have a file at that path.

```
OS error: [Errno 2] No such file or directory: 'somefile/path.txt'
```

## Debugging

Now we will learn how to use the debugger in PyCharm.

Most new programmers are surprised to find how long the find debugging, or fixing, the programs they write compared to writing them.  Errors in computer programs are called bugs, and one of the tools we use to look for them is called a debugger.

PyCharm has a built-in debugger. To start it you click the bug icon near the top right in the toolbar, or select  the 'Debug' item from the Run drop-down menu.  This depends on you having already setup a run configuration where you tell PyCharm what module you want to run.

A debugger lets you stop execution of your code and look at the current values of variables at the current point in the code. You can step through your code one statement at a time. You can also set breakpoints on certain lines of code and let the debugger stop whenever it reaches one of them. These are two of the main ways you control the debugger.  When you are stepping you can step over, into, or out of. Stepping over a function call line will not send the debugger into the function, but when you choose step into, you will go into each function call and be able to step through each line of its source code as well. When you choose step out of, the debugger runs until the current function returns.

When you are stopped in the debugger (not running) then you can look at the current value of variables that are in scope by hovering over them with the mouse cursor. You can also type them in the Variables pane by clicking plus and typing their name.

You can also evaluate Python expressions by opening the Expressions Window (Alt+F8 or select "Evaluate Expression..." from the Run menu) and entering them there. They will be evaluated in the current scope, meaning as if they were directly in the current place in the code.

## Project

We are going to make a program to read a text file and print the contents one line at a time. Each time the user presses space we will print one more line.

For extra credit you can also read the file's path from the user with input() before opening it instead of hard-coding it into your program.

## References

* <https://docs.python.org/3/reference/import.html>
* <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>
* <https://docs.python.org/3/tutorial/errors.html>
* <https://docs.python.org/3/library/functions.html#input>
* <https://docs.python.org/3/library/stdtypes.html#str.format>
