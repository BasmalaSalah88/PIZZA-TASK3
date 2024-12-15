from pizza import Margherita, Pepperoni, Cheese, Olives, Mushrooms
from order import Order
from inventory import Inventory
from payment import Payment

def main():
    inventory = Inventory()

  
    margherita = Margherita()
    pepperoni = Pepperoni()

    
    margherita = Cheese(margherita)
    margherita = Olives(margherita)

   
    order = Order()
    order.add_item(margherita)
    order.add_item(pepperoni)

   
    for topping in ["Cheese", "Olives"]:
        if inventory.check_availability(topping):
            inventory.reduce_ingredient(topping)

    
    print("Order Description:\n", order.get_description())
    print("Total Cost: $", order.get_total_cost())

   
    payment = Payment()
    print(payment.process_payment("PayPal", order.get_total_cost()))

if __name__ == "__main__":
    main()
