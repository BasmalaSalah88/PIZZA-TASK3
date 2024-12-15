
class Inventory:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.ingredients = {
                "Cheese": 10,
                "Olives": 10,
                "Mushrooms": 10,
            }
        return cls._instance

    def check_availability(self, ingredient):
        return self.ingredients.get(ingredient, 0) > 0

    def reduce_ingredient(self, ingredient):
        if self.check_availability(ingredient):
            self.ingredients[ingredient] -= 1
            return True
        return False
