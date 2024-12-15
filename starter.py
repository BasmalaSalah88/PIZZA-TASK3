from abc import ABC, abstractmethod

class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory


class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita"

    def get_cost(self) -> float:
        return 5.0


class Pepperoni(Pizza):
    def get_description(self) -> str:
        return "Pepperoni"

    def get_cost(self) -> float:
        return 6.0



class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza


class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self.pizza.get_description()}, Cheese"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 1.0


class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self.pizza.get_description()}, Olives"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.5


class Mushrooms(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self.pizza.get_description()}, Mushrooms"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.7


class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str, inventory: InventoryManager) -> Pizza:
        if pizza_type == "1" and inventory.check_and_decrement("Margherita"):
            return Margherita()
        elif pizza_type == "2" and inventory.check_and_decrement("Pepperoni"):
            return Pepperoni()
        else:
            print("Pizza unavailable or out of stock!")
            return None


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class PayPal(PaymentMethod):
    def pay(self, amount: float):
        print(f"Payment of ${amount:.2f} completed using PayPal. Thank you for your order!")


class CreditCard(PaymentMethod):
    def pay(self, amount: float):
        print(f"Payment of ${amount:.2f} completed using Credit Card. Thank you for your order!")


class PaymentFactory:
    @staticmethod
    def get_payment_method(method: str) -> PaymentMethod:
        if method == "1":
            return PayPal()
        elif method == "2":
            return CreditCard()
        else:
            print("Invalid payment method!")
            return None



def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        pizza = PizzaFactory.create_pizza(pizza_choice, inventory_manager)
        if not pizza:
            continue

        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                pizza = Cheese(pizza)
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                pizza = Olives(pizza)
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")
        payment_method = PaymentFactory.get_payment_method(payment_choice)
        if payment_method:
            payment_method.pay(pizza.get_cost())

        
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
