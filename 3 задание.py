class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_info(self):
        return f"{self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)  
        self.num_doors = num_doors  
    
    def get_info(self):
        base_info = super().get_info()  
        return f"{base_info}, {self.num_doors} дверей"


class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)  
        self.type = type 
    
    def get_info(self):
        base_info = super().get_info()  
        return f"{base_info}, тип: {self.type}"
    


if __name__ == "__main__":
    vehicle = Vehicle("Toyota", "Camry")
    car = Car("Toyota", "Camry", 4)
    bicycle = Bicycle("Trek", "Marlin 5", "горный")
    
    
    print("Базовый транспорт:")
    print(vehicle.get_info())  
    
    print("\nАвтомобиль:")
    print(car.get_info())  
    
    print("\nВелосипед:")
    print(bicycle.get_info())  
    
    #Дополнительные примеры
    car2 = Car("Honda", "Civic", 2)
    bicycle2 = Bicycle("Giant", "Escape 3", "городской")
    
    print("\nДругие транспортные средства:")
    print(car2.get_info())  

    print(bicycle2.get_info())  
