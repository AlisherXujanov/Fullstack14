lesson = "Class  &&  OOP"
_1 = 'Abstract and Inheritance'

# this == self

# class User:
#     def __init__(self, name:str='...'):
#         print(f"User {name} is created")
#         self.name = name

# user1 = User("John")
# print(user1)
# print(user1.name)


# DUNDER METHOD 1st
# __init__  => is a constructor method which is used to initialize the attributes of a class
# it is called automatically when an object is created
# RU: __init__ - это метод-конструктор, который используется для инициализации атрибутов класса
# он вызывается автоматически при создании объекта
#############################################################################################
################ Abstraction

# "abc" here stands for abstract base class. It is first imported and then used as 
# a parent class for some class that becomes an abstract class. Its simplest implementation 
# can be done as below.

# -------------------------------------
# class A:
#     name = "..."
    
# class B(A):
#     ...

# b = B()
# print(b.name)
# -------------------------------------

# from abc import ABC, abstractmethod
# class AbcAnimal(ABC):
#     def __init__(self, _name:str, _favorite_food:str) -> None:
#         self.name = _name
#         self.favorite_food = _favorite_food

#     def __str__(self):
#         return f"{self.name} eats {self.favorite_food}"

#     @abstractmethod
#     def get_description(self):
#         pass
#         # raise NotImplementedError

# class Pets(AbcAnimal):
#     def __init__(self, name, favorite_food, speed):
#         super().__init__(name, favorite_food)
#         self.speed = speed

#     def get_description(self):
#         return f"{self.name} eats {self.favorite_food} and runs at {self.speed} km/h"


# dog = Pets("Dog", "Meat", 10)
# print(dog)
# print(dog.get_description())


# abs module is used to create abstract classes
# it is helpful when we want to create a class that will be used as a base class
# abstractmethod is used to declare abstract methods which will be implemented by the child classes
# is it used to ensure that the child classes will have the same method as the parent class
# and returns an error if the child class does not have the same method as the parent class
# RU: абстрактный класс - это класс, который не предназначен для создания экземпляров,
# а предназначен для использования в качестве родительского класса для других классов
# абстрактный метод - это метод, который объявлен, но не реализован в базовом классе.

#############################################################################################
################ Inheritence

# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# is a way of creating a new class for using details of an existing class without modifying it.
# The newly formed class is a derived class (or child class).
# Similarly, the existing class is a base class (or parent class).
# from abc import ABC, abstractmethod

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def test(self):
#         print("Hello world")

# class Child(Parent, ABC):
#     #     Inherited members from parent class
#     #     Additional members of the child class
#     def __init__(self, name, age):
#         super().__init__(name)  # => calls the parent class constructor
#         self.age = age

#     def test(self):
#         print("Hello world from child")

#     def __repr__(self) -> str:
#         '''
#             Is used to represent the object with a string.
#             It is used for debugging and logging.
#         '''
#         return f"{self.name} is {self.age} years old"

    # def __str__(self) -> str:
    #     '''
    #         Is used to represent the object with a string.
    #         It is used for the end user.
    #     '''
    #     return f"{self.name} is {self.age} years old"


# child = Child("John", 20)
# print(child)
# print(child.test())
# ================================================================================
# ================================================================================
# USECASEs
class Animal:
    def __init__(self, name:str, speed:int, wild:bool=False) -> None:
        """
            name: str   =>  name of any type of animal
            speed: int  =>  running-or-flying speed of animal
            wild: bool  =>  defaults to False as it is not wild (Дикий)
        """
        self.name = name
        self.speed = speed
        self.wild = wild
        
    def __str__(self) -> str:
        wild = "wild" if self.wild else "not wild"
        return f"{self.name} can run {self.speed} km/h and is {wild}"


tiger = Animal("White Tiger", 60, True)
print(tiger)
print("=====================================================================")


class Bird(Animal):
    def __init__(self, name: str, speed: int, wild: bool, can_fly:bool=True):
        super().__init__(name, speed, wild)
        self.can_fly = can_fly


    def __str__(self) -> str:
        if self.can_fly:
            wild = "wild" if self.wild else "not wild"
            return f"{self.name} can fly at {self.speed} km/h and is {wild}"
        else:
            return super().__str__()
        
        
eagle = Bird("Eagle", 100, True)
penguin = Bird("Penguin", 20, False, False)
ostrich = Bird("Ostrich", 60, False, False)

print(eagle)
print(penguin)
print(ostrich)


