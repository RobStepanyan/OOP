# OOP
* Summaries, highlights, insights and code examples of "Python: Master the Art of Design Patterns"
* Other exercises, demonstrations and examples


### Recap
* Object-oriented analysis (**OOA**)
* Object-oriented design (**OOD**)
* Object-oriented programming (**OOP**)
* Unified Modeling Language (**UML**)
* **Classes** describe **objects**.
* The model is an **abstraction** of a real concept.
* **Abstraction** is the process of **encapsulating** information with separate public and private **interfaces**. The private interfaces can be subject to **information hiding**.
* **Composition** is the act of collecting several objects together to create a new one.
* **Aggregation** is almost exactly like **composition**. The difference is that aggregate objects can exist independently.
* **Polymorphism** is the ability to treat a class differently depending on which subclass is implemented.
* **Attribute** of an **object** is called **property**, while **attribute** of a **class** is still called **attribute**
* object.**__ dict __** and **vars**(object) both return properties of an objet as
 a dictionary
* **dir**(object) and object.**__ dir __** both return attributes (including 
properties) of an object and methods as a **list of variable names**.
* **setattr**(**object**, attr_name, value) sets attribute of an object (property), 
and **setattr**(**class_name**, attr_name, value) sets attribute of a class.
* **__ iter __ return self** to make a class an **iterator**.
* **__ next __** and **raise StopIteration**, next(obj) and obj.__ next __()
* **__ setitem __**(self, index, item)
* **__ getitem __**(self, index)
* **__ del __** finalizer.


## Table of Contents
### [Module 1: Python 3 Object-Oriented Programming - Second Edition](/Module1)
* [Chapter 1: Object-oriented Design](/Module1/Chapter1/README.md)
* [Chapter 9: The Iterator Pattern](/Module1/Chapter9/README.md)
