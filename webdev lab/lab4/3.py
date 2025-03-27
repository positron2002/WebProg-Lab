class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self):
        item_id = input("Enter Item ID: ")
        if item_id in self.items:
            print(f"Item with ID {item_id} already exists.")
        else:
            item_name = input("Enter Item Name: ")
            stock_count = int(input("Enter Stock Count: "))
            price = float(input("Enter Price: "))
            self.items[item_id] = {
                'item_name': item_name,
                'stock_count': stock_count,
                'price': price
            }
            print(f"Item {item_name} added successfully.")

    def update_item(self):
        item_id = input("Enter Item ID to update: ")
        if item_id in self.items:
            item_name = input("Enter new Item Name (leave blank to keep current): ")
            stock_count = input("Enter new Stock Count (leave blank to keep current): ")
            price = input("Enter new Price (leave blank to keep current): ")
            if item_name:
                self.items[item_id]['item_name'] = item_name
            if stock_count:
                self.items[item_id]['stock_count'] = int(stock_count)
            if price:
                self.items[item_id]['price'] = float(price)
            print(f"Item with ID {item_id} updated successfully.")
        else:
            print(f"Item with ID {item_id} does not exist.")

    def check_item_details(self):
        item_id = input("Enter Item ID to check: ")
        if item_id in self.items:
            item = self.items[item_id]
            print(f"Item ID: {item_id}")
            print(f"Item Name: {item['item_name']}")
            print(f"Stock Count: {item['stock_count']}")
            print(f"Price: {item['price']}")
        else:
            print(f"Item with ID {item_id} does not exist.")

def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Check Item Details")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            inventory.add_item()
        elif choice == '2':
            inventory.update_item()
        elif choice == '3':
            inventory.check_item_details()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
