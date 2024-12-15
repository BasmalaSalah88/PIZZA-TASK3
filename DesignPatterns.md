1.1 Decorator Pattern
The Decorator Pattern is used in our pizza ordering system to dynamically add toppings to pizzas.

Description:
The Decorator Pattern allows you to add new functionality to an object without changing its structure.
In our system, we used this pattern to create dynamic toppings like Cheese, Olives, and Mushrooms.
Application in the Pizza System:
We created a base Pizza class, which represents a pizza without toppings. Then we used the ToppingDecorator class to add toppings dynamically.
Each topping (e.g., Cheese, Olives) is a subclass of ToppingDecorator, which modifies the Pizza object by appending the topping’s description and increasing the price

c# The basic Pizza class, which represents a pizza with no toppings
class Pizza:
    def __init__(self):
        self.description = "Basic Pizza"
        self.cost = 5.00  # Base price for a basic pizza

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# The ToppingDecorator class, which will add toppings to the pizza dynamically
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza  # This stores the original pizza object

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


# The Cheese topping decorator
class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.00  # Add the cost of cheese


# The Olives topping decorator
class Olives(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Olives"

    def get_cost(self):
        return self.pizza.get_cost() + 0.50  # Add the cost of olives


# The Mushrooms topping decorator
class Mushrooms(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Mushrooms"

    def get_cost(self):
        return self.pizza.get_cost() + 0.70  # Add the cost of mushrooms

1.2 Over-Engineering Concept
Description:
Over-engineering refers to making a system more complex than necessary. It happens when additional features or structures are added to the system that are not needed for the task at hand.

Example of Over-Engineering in the Pizza System:
An example of over-engineering in our pizza system would be creating a separate class for every combination of pizza and toppings, like MargheritaCheeseOlivesPizza or PepperoniCheeseMushroomsPizza. This approach leads to unnecessary complexity because we can achieve the same functionality by using the Decorator Pattern
incorrect ex:

# Creating separate classes for every combination of pizza and toppings
class MargheritaCheeseOlivesPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza, Cheese, Olives"
        self.cost = 8.50  # Price for Margherita with cheese and olives


class PepperoniCheeseMushroomsPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pepperoni Pizza, Cheese, Mushrooms"
        self.cost = 9.50  # Price for Pepperoni with cheese and mushrooms
