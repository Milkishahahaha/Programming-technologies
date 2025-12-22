#Задание 1 (Инкапсуляция)

class Person:
    def __init__(self, name, age):
        self.__name = name    
        self.__age = age      

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Возраст должен быть положительным числом")


person = Person("Анна", 20)

print(person.get_name())  
print(person.get_age())   

person.set_name("Мария")
person.set_age(25)

print(person.get_name())  
print(person.get_age())   

