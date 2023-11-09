"""
OBJECT ORIENTED PROGRAMMING.
What is object oriented programming?
Object-oriented programming is a computer programming model  organizes software design around data, or objects,
rather than functions and logic.
 
An object is a data field that has unique attributes and behavior.

ADAVANTAGES OF USING OBJECT ORIENTED PROGRAMMING.
Modularity: OOP encourages the organisation of code into small , self contained object, making it easierto debug, 
            manitain, and make changes to code.
Reusability: promotes code reusability through the use of classes and inheritance. 
            Developers can create new classes by building upon existing ones, reducing the need to rewrite co
nterface Descriptions:

Explanation: OOP allows the description of interfaces, which define a contract for classes that implement them. 
             This ensures that classes that adhere to the same interface will provide specific functionality,
                enhancing code predictability and maintainability.
                
CLASSE:
a class is a template definition of the methods and variables in a particular kind of object. 
OR
A class is a blueprint or template for creating objects in OOP.


(Properties) in a Class:
Attributes:
are data members or properties that describe the characteristics of an object.
They represent the state of an object and are often referred to as instance variables.
For example, a "Car" class might have attributes like "color," "make," and "model."

 Methods (Functions) in a Class:
 Methods are functions defined within a class that define the behaviors of objects created from that class.
They operate on the attributes and data of the class.
For example, a "Car" class might have methods like "startEngine" and "stopEngine."

Object Creation:

Objects are instances of a class. They are created based on the blueprint provided by the class.

. Encapsulation:

Encapsulation is the principle of bundling the data (attributes) and methods (functions) that operate on
that data into a single unit, i.e., the object.
It also involves controlling the access to data by making some attributes private or protected and providing public
methods for interaction.

 Constructor:

A constructor is a special method in a class used to initialize the object's attributes when an object is created.
It has the same name as the class and is often used to set default values for attributes.
For example, a "Car" class might have a constructor to set the initial values of "make" and "model."

OBJECTS/INSTANCES
An instance is another term for an object in OOP.
It is an individual occurrence of a class, representing a unique entity within the program.

Object Creation:

Objects are created by instantiating a class.
This process involves allocating memory for the object and initializing its attributes based on 
the class's constructor.

 Methods of Objects:

Objects have methods, which are functions defined within the class.
Methods represent the behaviors or actions that objects can perform.
For instance, in a "Car" class, methods might include "startEngine" and "stopEngine."


"""

class User: # we define a class called User
    def __init__(self, name, age, location): # the 'init': is a constructor method for class.Its primary role is to initialize the object's attributes 
        self.name = name                     # self It allows you to access and modify object-specific attributes.
        self.age = age                       #we initialize the object's attributes using the values passed as arguments.
        self.location = location

              
# Creating a new instance of the User class
user1 = User("DEV. BREE", 16, "Namugongo")

# Accessing the user's name and age
user_name = user1.name
user_age = user1.age

# Printing the user's name and age
print("User Name:", user_name)
print("User Age:", user_age)

#function to print the user's location
user2_location=user1.location


# Printing the updated user's location
print("User Location:", user1.location) 


#METRHOD 2
class User:
    name = "Dev Bree"
    age= 16
    location="namugongo"
user1=User()
print(user1.name)
print(user1.age)
    
print(user1.location)
