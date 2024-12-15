
### Design Patterns and Their Relation to SOLID Principles

1. **Singleton Pattern: Inventory Manager**
   - **Description:** The **InventoryManager** class uses the Singleton pattern to ensure that there is only one instance managing the inventory throughout the application.
   - **Adheres to SOLID Principles:**
     - **Single Responsibility Principle (SRP):** The **InventoryManager** is solely responsible for managing the inventory of the pizza ingredients, ensuring that no other class takes on this responsibility.
     - **Dependency Inversion Principle (DIP):** The higher-level classes depend on the **InventoryManager** abstraction, rather than directly managing the inventory themselves.

2. **Factory Method: Pizza Creation**
   - **Description:** The **PizzaFactory** class implements the Factory Method pattern to abstract the process of creating different types of pizzas like **Margherita** and **Pepperoni**.
   - **Adheres to SOLID Principles:**
     - **Open/Closed Principle (OCP):** New types of pizzas can be added without modifying the existing pizza creation logic, adhering to the open/closed principle.
     - **Single Responsibility Principle (SRP):** The **PizzaFactory** is dedicated only to the creation of pizzas, keeping the codebase organized and focused.

3. **Decorator Pattern: Adding Toppings**
   - **Description:** The **ToppingDecorator** class and its subclasses (like **CheeseTopping**, **OliveTopping**, etc.) allow adding toppings to a pizza object dynamically, without altering the pizza class itself.
   - **Adheres to SOLID Principles:**
     - **Open/Closed Principle (OCP):** New toppings can be easily added by creating new decorator classes, without modifying the existing pizza or topping classes.
     - **Liskov Substitution Principle (LSP):** Each topping decorator conforms to the **Pizza** interface, meaning they can be substituted seamlessly in the system.

4. **Strategy Pattern: Payment Methods**
   - **Description:** The **PaymentMethod** interface allows different payment strategies (like **PayPalPayment** and **CreditCardPayment**) to be used interchangeably, letting the user choose the payment method at checkout.
   - **Adheres to SOLID Principles:**
     - **Open/Closed Principle (OCP):** New payment methods can be added without altering the existing payment logic.
     - **Interface Segregation Principle (ISP):** Each payment class focuses solely on the payment process and doesn't implement irrelevant methods.
     - **Dependency Inversion Principle (DIP):** The system depends on the **PaymentMethod** abstraction, rather than specific implementations, enabling easier extensions and modifications.
