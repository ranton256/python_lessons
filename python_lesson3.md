# Python Lesson three

## Object Oriented Programming (OOP)

Objects are a way of representing more complex data structures together with functionality on them.

In traditional structured programming, the predominant model before object oriented programming, data structures were modeled separately from the procedures or functions which used or modified them.

With objects, these two aspects, data and code, are combined under the same roof so to speak of objects.

Most languages which support object oriented programming also support procedural programming as well.

Python supports object oriented programming, though it does not force you to use it.

In object oriented programming, everything is an object. How strictly this everything is meant depends on the specific programming language.

## Objects and Classes

A class represents a type of things. In fact, in object oriented programming languages, a specific class is considered a type, just like an integer or string(and string is often a class).

An object is an instance of a specific class. For example, Cat could be a class and Anna would a particular instance(aka object) of the class Cat.

An object instance contains specific fields(basically variables) that are part of each instance of the object. These are also called member variables.  These hold the data parts of the object.

Classes have member methods which are procedures(aka functions or routines) which operate on an instance of the class and have access to that object's member variables.

In Python, there is a special variable, *self*, which is passed as the first parameter to a member method of a class. This variable points to the object/instance itself, and is how you access the object's member variables and other member methods.

There are also class level variables and methods as opposed to instance level, but we will talk about those later.

In Python, everything is an object. You can find out the type of an object using the `type` function.

```python
type("blah")
```

That will print out something like this:

> type("blah")
> <class 'str'>

A constructor is the method which sets up an instance of a new object.

In Python, constructors have a special name,  `__init__`.

Let's look `at` an example.

```python
 """Vehicle example"""




class Vehicle:
    """This class represents any type of vehicle with max speed, seating and weight."""
    def __init__(self, max_speed, weight, seating_capacity):
        # set member variables (attributes or fields)
        self.max_speed = max_speed
        self.weight = weight
        self.seating_capacity = seating_capacity
        self.passengers = []
        self.speed = 0.0

    def get_weight(self):
        return self.weight

    def get_max_speed(self):
        return self.max_speed

    def get_speed(self):
        return self.speed

    def accelerate(self, amount):
        self.speed = self.speed + amount
        if self.speed < 0.0:
            self.speed = 0.0
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def speed_up(self):
        self.accelerate(10)

    def slow_down(self):
        self.accelerate(-10)

    def get_seating_capacity(self):
        return self.seating_capacity

    def add_passenger(self, passenger_name):
        if len(self.passengers) >= self.get_seating_capacity():
            return False  # or we could throw an exception here.
        else:
            self.passengers.append(passenger_name)

    def get_passengers(self):
        return self.passengers.copy()

    def __str__(self):
        return "Vehicle(max_speed: {}, weight: {}, seats: {}, speed: {}, passengers: {}".format(
            self.max_speed, self.weight, self.seating_capacity, self.speed,
            ",".join(self.passengers)  # comma separated list of passengers
        )

class Bicycle(Vehicle):

    def __init__(self):
        # This requires Python 3 or newer.
        super().__init__(30, 40, 1)

    def __str__(self):
        bs = super().__str__()
        return "Bicycle: " + bs



def main():
    my_vehicle = Vehicle(40.0, 2800, 4)
    print ("My vehicle is {}". format(my_vehicle))
    my_vehicle.add_passenger("Richard")
    print("The passengers are {}".format(my_vehicle.get_passengers()))
    print("My vehicle is {}".format(my_vehicle))
    for i in range(5):
        my_vehicle.speed_up()
        print("My vehicle is {}".format(my_vehicle))
    for i in range(5):
        my_vehicle.slow_down()
        print("My vehicle is {}".format(my_vehicle))

    my_bike = Bicycle()
    my_bike.add_passenger("Richard")
    print("My bike is {}".format(my_bike))

if __name__ == "__main__":
    # execute only if run as a script
    main()

```

Classes versus instances - A class is the type of thing. It's the definition of an object type, including properties(data it has)
and methods(behaviors/functionality it provides).  On the other hand, an instance is a specific thing which is of the specific type.
So you can have a Car class, and a variable named myCar which refers to an instance of the type Car.

Encapsulation - this is the bundling of data with the methods(functions) that operate on the data.
It is used to hide values (also known as state) of an object inside a class and prevent unauthorized access.
This is called data hiding or data protection. It is mainly convention (rather than enforced) in Python.

* in python declare methods or attributes protected using a single underscore before their name. This is just a convention.
* if you use double underscore as ap refix then it is not accessible.

Inheritance - one class gets methods and properties of a parent class. The child is called the subclass, and the parent is called the superclass.
The child can override methods to change behavior.

Composition - this is where you create one object out of multiple other objects by including them, i.e. as properties/attributes rather than by
inheriting from them. All things equal, if you aren't sure use composition rather than inheritance.

Polymorphism - this means mmany forms. It returns to different objects in the same class hierarch( parent/child/siblings/grandchild/etc) having different
behavior for the same methods.

Override - when a child class (subclass) defines the same method name, but with a different implementation it changes the behavior of object instances
of the subclass when that method is called. This is an override.

Overload - when multiple methods have the same name, but different parameters, this is called overloading.
Python does NOT directly support method or function overloading, but you can easily fake it with optional named parameters.

Abstract classes - a class which does not define some methods, but leaves them to be implemented by children is abstract.
In Python this is done by using the @abstractmethod decorator from the abc module and inheriting from the ABC class which
stands for abstract base class. In many programming languages abstract methods are a syntactical feature instead of
implemented via a separate module like ABC. For example C++ has pure virtual functions that provide this mechanism.

Class attributes and instance attributes

* A class can have an attribute which has a single value for the entire type NOT per instance.
* Instance attributes have a separate copy for each instance of the class.

Static, class methods and instance methods

* A normal object method in Python operates on a specific instance of the class.
* Python class method operates on the class itself, and uses the @classmethod decorator in Python. The first parameter is the class object, instead of an instance object. Usually this is called 'cls' rather than 'self'.
* A static method uses the @staticmethod decorator and is in the namespace of a class, but doesn't get passed class or instance as a parameter.

```python


#!/usr/bin/python

class Methods:
    cls_attr = 'in the class'

    def __init__(self, val):
        self.inst_attr = val


    def inst_method(self):
        print("I'm an instance: value={}".format(self.inst_attr))

    @classmethod
    def cls_method(cls):
        print("I'm a class: value={}".format(cls.cls_attr))


    @staticmethod
    def static_method():
        print("I'm a static method!")


def main():
    obj = Methods('from my instance')

    obj.inst_method()
    Methods.cls_method()
    Methods.static_method()

if __name__ == "__main__":
    # execute only if run as a script
    main()


```

Project:  make an object in a separate module that manages Todo lists as in last project, but handle item status (done or not) and adding or deleting items besides also listing them. After each change save the updated file.

## References

* <https://python-textbok.readthedocs.io/en/1.0/Classes.html>
* <https://realpython.com/python3-object-oriented-programming/>
* <https://dev.to/jckuhl/on-automobiles-and-oop-1k1k>
* <https://medium.com/the-renaissance-developer/python-101-object-oriented-programming-part-1-7d5d06833f26>
* <https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/>
* <https://realpython.com/courses/python-method-types/>
