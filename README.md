# Concepts in Object Oriented Programming

## Class

-template (blueprint) for the creation of an object

### `__init__` (initilizer)
- Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created.


### Attributes (Parameter)
- dectriptions of the object
- instance attribute (first_name)
- class - level attribute (WSU)

### Methods (Action)
- instance method
    - method that can be performed on the object
- class method
    - allows us to create and modify class level data
- static method
    - does not have access to class or instance attributes but performs actions within the class (format student id fuction in students file)
- magic method
    - reserved methods that perform a specific task `__str__`

## Inheritance
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
- Parent Class (Student)
- Child class (Graduate Student)

## Polymorphism
- Methods/fuctions/operators with the same name that can be executed on many objects or classes