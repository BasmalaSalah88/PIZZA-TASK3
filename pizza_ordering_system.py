class Pizza:
    def __init__(self):
        self.description = "Basic Pizza"
        self.cost = 5 

    def add_topping(self, topping):
        self.description += f", {topping.description}"
        self.cost += topping.cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 7  
class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pepperoni Pizza"
        self.cost = 8  
margherita = Margherita()
print(margherita.get_description())  
print(margherita.get_cost()) 
pepperoni = Pepperoni()
print(pepperoni.get_description()) 
print(pepperoni.get_cost())  