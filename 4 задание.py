# 4 задание
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.products = [] 

    def add_product(self, product):
        self.products.append(product)

    def get_total_price(self):
        total=0
        for product in self.products:
            total += product.price
        return total

    def display_order(self):
        print(f"Заказ №{self.order_number}")
        print("Список товаров:")

        if not self.products:
            print("  (товаров нет)")
        else:
            for product in self.products:
                print(f"-{product.name}: {product.price} руб.")

        print(f"Общая сумма: {self.get_total_price()} руб.")

p1 = Product("Хлеб", 50)
p2 = Product("Молоко", 80)
p3 = Product("Сыр", 200)

order = Order(1)
order.add_product(p1)
order.add_product(p2)
order.add_product(p3)

order.display_order()


