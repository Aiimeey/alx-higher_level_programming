## 0x0A. Python - Inheritance

### Description

This project is part of the Holberton School curriculum and focuses on the concept of inheritance in Python. Inheritance is a fundamental feature of object-oriented programming that allows you to create new classes that are based on existing classes. This project covers various aspects of inheritance in Python, including superclass and subclass relationships, method overriding, and more.

### Concepts

    Inheritance in Python
    Superclass and Subclass
    Method Overriding
    Class Attributes and Methods
    isinstance, issubclass, type, and super built-in functions

### Tasks

    Lookup: Write a function that returns the list of available attributes and methods of an object.

    My List: Create a class MyList that inherits from the list class and adds a method to print the list sorted in ascending order.

    Same Class or Inherit From: Write a function that checks if an object is an instance of a specified class or its subclasses.

    Only Sub Class of: Write a function that checks if an object is an instance of a class that inherited (directly or indirectly) from a specified class.

    Geometry Module: Create an empty class BaseGeometry to serve as a base class for geometric shapes.

    Improve Geometry: Enhance the BaseGeometry class by adding an area method that raises an Exception with the message "area() is not implemented."

    Integer Validator: Extend the BaseGeometry class by adding an integer_validator method that validates an attribute to ensure it is a positive integer.

    Rectangle: Create a Rectangle class that inherits from BaseGeometry and represents a rectangle with width and height attributes.

    Full Rectangle: Enhance the Rectangle class by implementing the area method and modifying the __str__ method to display the rectangle's dimensions.

    Square #1: Create a Square class that inherits from Rectangle and represents a square with a single side length.

    Square #2: Modify the Square class to have a custom string representation, displaying it as "[Square] <width>/<height>."

    My Integer: Create a class MyInt that inherits from int but reverses the equality operators (== and !=).

    Can I?: Write a function add_attribute that adds a new attribute to an object if it's possible, raising a TypeError if the object can't have a new attribute.
