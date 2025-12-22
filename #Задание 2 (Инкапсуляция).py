#Задание 2 (Инкапсуляция)

class Natural:
    def __init__(self, n):
        self.__number = None
        self.number = n  

    def __test(self, value):
        if type(value) is int and value > 0:
            return value
        else:
            print(f"Значение {value} было преобразовано к 1")
            return 1
    
    def number(self):
        return self.__number

    def number(self, value):
        self.__number = self.__test(value)

a = Natural(34)
b = Natural(-250)
c = Natural("Hello")

print(a.number, b.number, c.number)

a.number = -10     
print(a.number)

a.other = "тест"  
print(a.other)

