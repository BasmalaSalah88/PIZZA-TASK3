SOLID Principles and Design Patterns
1. Single Responsibility Principle (SRP):
Each class has one job. For example, the Pizza class represents the pizza, while the ToppingDecorator class is responsible for adding toppings.
2. Open/Closed Principle (OCP):
We can add new toppings or pizzas without changing existing code. For instance, we can add new topping classes or pizza types without modifying the Pizza class.
3. Liskov Substitution Principle (LSP):
We can substitute any pizza subclass (e.g., MargheritaPizza, PepperoniPizza) in the order system without breaking it.
4. Interface Segregation Principle (ISP):
We separate the responsibilities by using specific interfaces for different classes (e.g., PaymentStrategy for payment methods).
5. Dependency Inversion Principle (DIP):
The Order class depends on abstractions (e.g., Pizza and PaymentStrategy), not concrete classes. This makes it easier to change the pizza or payment methods