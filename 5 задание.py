# 5 задание
class Animal:
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

class Dog(Animal):
    def make_sound(self):
        return "Гав!"

class Cow(Animal):
    def make_sound(self):
        return "Муу!"

def zoo_concert(animals_list):
    for animal in animals_list:
        print(animal.make_sound())

animals = [Cat(), Dog(), Cow()]
zoo_concert(animals)
