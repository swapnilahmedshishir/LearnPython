from abc import ABC , abstractmethod

class Bank(ABC):
    @abstractmethod
    def transaction(self , amount):
        pass
    @abstractmethod
    def balance(self):
        pass

class SavingsAccount(Bank):
    def __init__(self , balance):
        self._balance= balance
    def transaction(self, amount):
        self._balance -= amount
        print(f"{amount} Taka Withdrawn")
    def balance(self):
         print(f"Current balance: {self._balance} taka")


class CurrentAccoutn(Bank):
    def __init__(self , balance):
        self._balance = balance
    def transaction(self, amount):
        self._balance -= amount
        print(f"{amount} taka withdrawn (from Current Account).")
    def balance(self):
         print(f"Current balance: {self._balance} taka")


acc1 = SavingsAccount(1000)
acc1.transaction(200)
acc1.balance()


acc2 = CurrentAccoutn(5000)
acc2.transaction(1500)
acc2.balance()