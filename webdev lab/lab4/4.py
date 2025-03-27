class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = {}
        self.customer_orders = {}

    def add_item_to_menu(self):
        item_id = input("Enter Item ID: ")
        item_name = input("Enter Item Name: ")
        price = float(input("Enter Price: "))
        self.menu_items[item_id] = {'item_name': item_name, 'price': price}
        print(f"Item {item_name} added to the menu.")

    def book_tables(self):
        table_id = input("Enter Table ID: ")
        customer_name = input("Enter Customer Name: ")
        self.book_table[table_id] = customer_name
        print(f"Table {table_id} booked for {customer_name}.")

    def customer_order(self):
        order_id = input("Enter Order ID: ")
        table_id = input("Enter Table ID: ")
        item_id = input("Enter Item ID: ")
        quantity = int(input("Enter Quantity: "))
        if table_id in self.book_table and item_id in self.menu_items:
            if order_id not in self.customer_orders:
                self.customer_orders[order_id] = []
            self.customer_orders[order_id].append({'table_id': table_id, 'item_id': item_id, 'quantity': quantity})
            print(f"Order {order_id} placed for Table {table_id}.")
        else:
            print("Invalid Table ID or Item ID.")

    def print_menu(self):
        print("\nMenu:")
        for item_id, details in self.menu_items.items():
            print(f"Item ID: {item_id}, Item Name: {details['item_name']}, Price: {details['price']}")

    def print_table_reservations(self):
        print("\nTable Reservations:")
        for table_id, customer_name in self.book_table.items():
            print(f"Table ID: {table_id}, Customer Name: {customer_name}")

    def print_customer_orders(self):
        print("\nCustomer Orders:")
        for order_id, orders in self.customer_orders.items():
            print(f"Order ID: {order_id}")
            for order in orders:
                item_name = self.menu_items[order['item_id']]['item_name']
                print(f"  Table ID: {order['table_id']}, Item Name: {item_name}, Quantity: {order['quantity']}")

def main():
    restaurant = Restaurant()
    while True:
        print("\nRestaurant Management System")
        print("1. Add Item to Menu")
        print("2. Book Table")
        print("3. Take Customer Order")
        print("4. Print Menu")
        print("5. Print Table Reservations")
        print("6. Print Customer Orders")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            restaurant.add_item_to_menu()
        elif choice == '2':
            restaurant.book_tables()
        elif choice == '3':
            restaurant.customer_order()
        elif choice == '4':
            restaurant.print_menu()
        elif choice == '5':
            restaurant.print_table_reservations()
        elif choice == '6':
            restaurant.print_customer_orders()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
