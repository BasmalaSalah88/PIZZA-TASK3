
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, pizza):
        self.items.append(pizza)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items)

    def get_description(self):
        return "\n".join(item.get_description() for item in self.items)
