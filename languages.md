Programming Languages
=====================

There are many different programming languages in common use today, and many more
specialized ones as well.  Programming languages can be grouped based on some
basic decisions in their design.

Machine Language
----------------

These are the binary coded instructions used directly by the processor.
Typically the only people working with machine language, are writing
assemblers or compilers to generate machine language (more on those later).
Each instruction set architecture, basically family of processors, has its own
unique assembly language.  Some of the most common currently are Intel x86 and ARM.

Assembly Language
-----------------

Assembly language provides a set of more human friendly mnemonics (which
means a thing easy to remember) that translates directly to machine language.
Assembly language is transformed to machine language by a program called an
assembler. Except for some special cases one assembly language instruction,
which goes on a single line, translates directly to one corresponding machine
language instruction.  There was a time when personal computers were slow
enough that a great deal of software was written in assembly for performance
reasons, because this is the most efficient form of programming, at least for
someone highly competent at it.  Early video game consoles also were typically
programmed in assembly due to limited resources and computing power.

Interpreted Languages
---------------------

Interpreted programming languages execute directly from their source by
running inside a program called an interpreter that executes the instructions
on behalf the language.  These languages are typically faster to develop code
in but result in much slower code than compiled languages.

Compiled Languages
------------------

Compiled languages are compiled by a program called, you guessed it, a
compiler, directly into machine language for the target processor.  Compiled
languages usually offer the best performance, but less flexibility than most
interpreted languages.  Flexibility is sometimes a help and sometimes a
hindrance in programming.  It can often lead to code being written faster but
being harder to execute efficiently or test completely.

Bytecode Languages
------------------

There is a type of language in between compiled and interpreted that uses
bytecode similar to machine language for an imaginary, simplified processor as
the output of its compiler.  This bytecode is either interpreted to execute
it, or it is run through a just-in-time compiler, JIT, to translate it to
native machine code just before execution.  This is most commonly associated
with Java which is extremely popular with both beginners, students, and
professionals.  Java was not however the first, or even the first popular
bytecode based programming language. The first popular bytecode compiler was
the UCSD Pascal which generated a bytecode called p-Code.

Dynamic Typing
--------------

Another key difference between programming languages is whether they are
statically or dynamically typed.  A language which is dynamically typed has
variables (variables are holders for values, more on that later) which can
accept any value or only certain types of values.  For example, in a
dynamically typed language one variable could hold an integer(same meaning as
in algebra, a number with no fractional or decimal part) or a floating point
value (the normal way of representing numbers with something to the right of
the decimal place), or a string (which is an ordered list of characters as in
letters, numbers, spaces, and punctuation).

Static Typing
-------------

In a language with static typing, variables are declared to be of a certain
type when created, and from then on they can only be assigned values of that
type. For example, it would be an error to try and put a string into an integr
variable in a statically typed language.  The advantage of statically typed
languages is that it is easier to ensure your code is correct at compile time,
and easier to compile or (less frequently) interpret the code efficiently. Of
course you lose flexibility in return for those advantages.

Procedural
----------

Procedural languages are those where you call a procedure, you pass it some
values, and it does some work and possibly returns a result.  Many languages
which are really procedural call things which return a result functions, but
beware of the terminology because functional programming means something else.

Functional Programming
----------------------

Functional programming languages such as the LISP family(mostly) and Haskell
use functions which are closer to the mathematical meaning of function.
Functions normally don't have side effects (with some excepts for input/output
methods), which means if you call a function with the same values, you will
always get the same result.  They also tend to take much more advantage of
recursion (functions calling themselves) including a special type called
tail recursion more than programs in other types of languages.

Object Oriented
---------------

Object oriented languages revolve around the concept of objects which are
basically a combination of data with procedures to operate on that data and
with other objects.  Depending on the language, you say that objects accept
messages or have methods that operate on them. These are really two ways of
describing the same thing.  Object oriented languages exploded in popularity
because they have features to help programmers insulate different parts of
large software systems from each other and reuse code more easily.
The typically cited four basic aspects of object-oriented programming are:

* Encapsulation - restricting access to data from outside the object and tying
  the data and methods which act on it together.
* Abstraction - defining objects which can be actors which perform work and
  communicate with each other.
* Inheritance - objects can be a more specialized type (subtype) of another object and
  inherit code and/or external interface
* Polymorphism - subtypes of the same parent can be treated interchangably. As
  long as the implement the agreed on methods, the code using them does not
  have to worry about which subtype they actually are.

Memory Management
----------------

There are two primary ways that memory is used in computer programs, the stack and the heap.

The stack is used for local variables allocated for each function or procedure call.
When a procedure/function(these terms are mostly interchangeable for computer programming) begins executing, it sets up a stack frame which moves the stack pointer the number of bytes required for its local variables. When the function returns it puts back the stack pointer to its prior location. So the stack pointer moves up and down as procedures call other procedures in a way that keeps track of all the local variables until they are no longer needed, meaning the function call which needed them is returning(finishing).

Memory on the heap must be allocated. This really just means it has to be set aside so it isn't accidentally used for some other purposes. When memory on the heap is finished
it must be deallocated. Deallocation is also known as freeing memory or releasing memory.

Some languages require the programmer to manage heap objects explicitly, such as C.
Other languages such as Lua, Java and Go manage the heap fore the programmer using
a system known as garbage collection. Some languages use a different method of managing
memory known as reference-counting, such as Python and Objective C.

<!-- TODO: graphics to demonstrate stack and heap usage. -->

Processes and Threads
---------------------

Modern computers can execute many programs in parallel.  An instance of a separate program while executing is called a process.  If you start two copies of the same program on most operating systems, you will actually have two processes.  

Each process has its own memory, both its own heap and its own stack.

Within a process, there can be separate sub-programs that can execute in parallel, meaning at the same time. In other words they run concurrently; these are called threads.
In most operating systems and most situations, threads within the same process share
the same heap but have a different stack.  They must have a different stack so that
the local variables for each thread's current procedure calls do not interfere
with each other.  However, using the same heap allows threads to communicate by sharing memory.  However, in order to do so safely without corrupting the data in memory
in unpredictable ways because of timing of the different threads, synchronization
methods must be used, such as mutual exclusion locks, usually called mutexes.

When a computer executes multiple processes or threads at once, it may actually suspend (put to sleep) some of the threads. For example if a computer with two CPU cores
wants to run four processes at once, only two will really be running on the CPUs
at any exact time, but the operating system will schedule them to take turns so that
they actually take turns using the CPU.

TODO: provide some references for where to learn more about operating systems
and concurrency.
