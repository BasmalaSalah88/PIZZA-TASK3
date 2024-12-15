# SOLID Principles and Design Patterns in the Pizza Restaurant Ordering System

## 1. Single Responsibility Principle (SRP)

### Description:
The **Single Responsibility Principle (SRP)** states that a class should have only one reason to change, meaning that it should have only one responsibility or function.

### Application in the Pizza System:
- The `Pizza` class is responsible for providing basic pizza information, such as its description and cost.
- The `ToppingDecorator` class is responsible for adding toppings to a pizza without modifying the original pizza class, maintaining a clear single responsibility for both classes.

### Code Example:
```python
class Pizza:
    def __init__(self):
        self.description = "Basic Pizza"
        self.cost = 5.00  

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

Description:
The Open/Closed Principle (OCP) states that a class should be open for extension, but closed for modification. This allows for adding new functionality without changing existing code.

Application in the Pizza System:
By using the Decorator Pattern, we can add new toppings (e.g., Cheese, Olives, Mushrooms) without modifying the Pizza class.
The Pizza class is closed for modification but can be extended by adding decorators to customize the pizza
class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.00
3. Liskov Substitution Principle (LSP)
Description:
The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

Application in the Pizza System:
The subclasses Margherita and Pepperoni can replace instances of the Pizza class without breaking the system.
Each subclass of Pizza (e.g., Margherita, Pepperoni) behaves as a valid instance of Pizza while extending the functionality with additional details specific to each type.
class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 6.00
4. Interface Segregation Principle (ISP)
Description:
The Interface Segregation Principle (ISP) states that no client should be forced to depend on methods it does not use. This encourages creating smaller, more specific interfaces instead of large, general ones.

Application in the Pizza System:
In this system, we don’t have a large interface, but we adhere to this principle by ensuring that each class has a specific responsibility.
The Pizza class is a simple interface with methods like get_description() and get_cost(), which are essential and are used across different types of pizzas.
class Pizza:
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

5. Dependency Inversion Principle (DIP)
Description:
The Dependency Inversion Principle (DIP) suggests that high-level modules should not depend on low-level modules. Instead, both should depend on abstractions. Additionally, abstractions should not depend on details, but details should depend on abstractions.

Application in the Pizza System:
We apply the DIP by depending on abstract Pizza and ToppingDecorator classes rather than concrete implementations.
The system can work with any Pizza subclass or decorator without being tightly coupled to any specific implementation.
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()
