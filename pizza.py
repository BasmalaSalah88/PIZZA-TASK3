class Pizza:
    def __init__(self):
        self.description = "Basic Pizza"
        self.cost = 5.00  

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.00


if __name__ == "__main__":
    pizza = Pizza()
    print(f"Description: {pizza.get_description()}")
    print(f"Cost: {pizza.get_cost()}")

    cheese_pizza = Cheese(pizza)
    print(f"Description with Cheese: {cheese_pizza.get_description()}")
    print(f"Cost with Cheese: {cheese_pizza.get_cost()}")




