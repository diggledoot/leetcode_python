from abc import ABC, abstractmethod


class Interface1(ABC):
    @abstractmethod
    def interface_method_1(self):
        print("Interface 1 default method")


class Interface2(ABC):
    @abstractmethod
    def interface_method_2(self):
        print("Interface 2 default method")


# __ means private (just that class, subclass cannot see), _ means protected (subclass and parent class)
class MyClass(Interface1, Interface2):
    def __init__(self, name: str = "Default", age: int = 0, gender: str = "T") -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def interface_method_1(self):
        print("Overrided interface 1 method")

    def interface_method_2(self):
        print("Overrided interface method 2")


myClass = MyClass()
myClass.interface_method_1()
myClass.interface_method_2()
print(myClass.get_name())
print(myClass.gender)
