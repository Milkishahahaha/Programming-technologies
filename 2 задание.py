class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number  
        self.__balance = 0 
    
    def deposit(self, amount):
        """Пополнение счета на указанную сумму"""
        if amount > 0:
            self.__balance += amount
        else:
            print("Сумма пополнения должна быть положительной")
    
    def withdraw(self, amount):
        """Снятие суммы со счета"""
        if amount <= 0:
            print("Сумма снятия должна быть положительной")
            return False
        
        if amount > self.__balance:
            print("Недостаточно средств")
            return False
        
        self.__balance -= amount
        return True
    
    def get_balance(self):
        """Получение текущего баланса"""
        return self.__balance



if __name__ == "__main__":
    account = BankAccount("1234567890")
    print(f"Начальный баланс: {account.get_balance()}")  
    
    account.deposit(1000)
    print(f"Баланс после пополнения: {account.get_balance()}")  
    
    account.withdraw(500)
    print(f"Баланс после снятия 500: {account.get_balance()}")  
    
    account.withdraw(1000)  
    print(f"Баланс после попытки снятия 1000: {account.get_balance()}")  
   
    print(f"Номер счета: {account.account_number}")  

  
