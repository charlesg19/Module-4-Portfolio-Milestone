class ItemToPurchase:
    def __init__(self):
        self.item_name = "None"
        self.item_price = 0
        self.item_quantity = 0
        
    def updateValues(self):
        self.item_name = input("Enter the item name: ")
        self.item_price = float(input("Enter the item price: "))
        self.item_quantity = int(input("Enter the item quantity: "))
        
    def print_item_cost(self):
        print(self.item_name, end=" ")
        print(self.item_quantity, end=" ")
        print("@ ${:.2f}".format(self.item_price), end=" ")
        self.total = self.item_price * self.item_quantity
        print("= ${:.2f}".format(self.total))
        

def main():
    item1 = ItemToPurchase()
    item1.updateValues()
    item2 = ItemToPurchase()
    item2.updateValues()
    
    print ("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    items_cost_sum = item1.total + item2.total
    print("Total: ${:.2f}".format(items_cost_sum))

if __name__ == "__main__":
    main()
