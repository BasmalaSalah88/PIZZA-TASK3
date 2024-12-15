1. Singleton Pattern
Description: The Singleton Pattern ensures only one instance of a class is created. In our case, we use it for the InventoryManager, which tracks the ingredients in the restaurant.
Before Pattern: Without this pattern, multiple instances of InventoryManager could have been created, causing inconsistencies in the inventory.
How It Improves the System: Using a Singleton guarantees that the inventory is managed consistently throughout the application, making it easier to track stock.
Code Example:
class InventoryManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self._inventory = {"Margherita": 10, "Pepperoni": 10}
    def check_and_decrement(self, item):
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False
2. Factory Method Pattern
Description: The Factory Method creates pizza objects based on the type selected (e.g., Margherita or Pepperoni).
Before Pattern: Without it, pizza creation would be hardcoded everywhere, making the system difficult to modify or extend.
How It Improves the System: It isolates the pizza creation logic, making it easier to add more pizza types later without changing the core logic.
Code Example:
class Pizza:
    def get_description(self): pass
    def get_cost(self): pass

class MargheritaPizza(Pizza):
    def get_description(self):
        return "Margherita Pizza"
    def get_cost(self):
        return 5.0

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Margherita":
            return MargheritaPizza()
3. Decorator Pattern
Description: The Decorator Pattern is used to add toppings to pizzas dynamically (e.g., cheese, olives).
Before Pattern: Without decorators, we'd need to modify the pizza class each time we added a new topping, which would make the system hard to maintain.
How It Improves the System: It allows toppings to be added independently, making it easy to extend the system
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza
    def get_description(self):
        return self._pizza.get_description()
    def get_cost(self):
        return self._pizza.get_cost()

class CheeseTopping(ToppingDecorator):
    def get_description(self):
        return self._pizza.get_description() + ", Cheese"
    def get_cost(self):
        return self._pizza.get_cost() + 1.0
4. Strategy Pattern
Description: The Strategy Pattern allows the payment method to be chosen dynamically (e.g., PayPal or Credit Card).
Before Pattern: Without this pattern, the payment logic would be embedded in the order process, making it hard to change.
How It Improves the System: It decouples the payment methods from the rest of the system, allowing easier addition of new payment methods.
class PaymentStrategy:
    def pay(self, amount): pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class Order:
    def __init__(self, pizza, payment_method):
        self.pizza = pizza
        self.payment_method = payment_method
    def complete_order(self):
        print(f"Total cost: ${self.pizza.get_cost()}")
        self.payment_method.pay(self.pizza.get_cost())
over Engineering (Simple Example)
Over Engineering happens when we add too much complexity to the system. For example, if we created a separate class for each topping type (like CheeseTopping, OliveTopping, etc.) instead of using the Decorator Pattern, we'd be making the system more complicated than necessary.

Example of Over Engineering:
class CheeseToppingDecorator(CheeseToppingDecorator):
    pass  