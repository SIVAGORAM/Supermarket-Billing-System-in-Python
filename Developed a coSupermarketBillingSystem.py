from datetime import datetime

def display_items(items):
    print("Current list of items:")
    for item, price in items.items():
        print(f"{item.capitalize()} Rs {price}/unit")

def main():
    name = input("Enter your name: ")

    price = 0
    pricelist = []
    totalprice = 0
    finalamount = 0

    ilist = []
    qlist = []
    plist = []

    items = {
        'rice': 20,
        'sugar': 30,
        'salt': 20,
        'oil': 80,
        'paneer': 110,
        'maggi': 50,
        'boost': 90,
        'colgate': 85
    }

    while True:
        print("\nOptions:\n1. Display list of items\n2. Add new item\n3. Purchase items\n4. Exit")
        main_choice = int(input("Enter your choice: "))
        if main_choice == 1:
            display_items(items)
        elif main_choice == 2:
            new_item = input("Enter new item name: ").lower()
            if new_item in items:
                print("Item already exists.")
            else:
                new_price = int(input(f"Enter price for {new_item}: "))
                items[new_item] = new_price
                print(f"Item {new_item} added with price Rs {new_price}.")
        elif main_choice == 3:
            while True:
                display_items(items)
                inp1 = int(input("If you want to buy press 1 or 2 for exit: "))
                if inp1 == 2:
                    break
                if inp1 == 1:
                    item = input("Enter your item: ").lower()
                    if item in items.keys():
                        quantity = int(input("Enter quantity: "))
                        price = quantity * items[item]
                        pricelist.append((item, quantity, items[item], price))
                        totalprice += price
                        ilist.append(item)
                        qlist.append(quantity)
                        plist.append(price)
                    else:
                        print("Sorry, the entered item is not available.")
                else:
                    print("You entered the wrong number.")
            
            while True:
                print("\nOptions:\n1. Remove item\n2. Update quantity\n3. Finalize Bill")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    item_to_remove = input("Enter the item to remove: ").lower()
                    if item_to_remove in ilist:
                        index = ilist.index(item_to_remove)
                        totalprice -= plist[index]
                        del ilist[index]
                        del qlist[index]
                        del plist[index]
                        print(f"{item_to_remove} removed from the list.")
                    else:
                        print("Item not found in the list.")
                elif choice == 2:
                    item_to_update = input("Enter the item to update quantity: ").lower()
                    if item_to_update in ilist:
                        index = ilist.index(item_to_update)
                        new_quantity = int(input("Enter new quantity: "))
                        totalprice -= plist[index]
                        new_price = new_quantity * items[item_to_update]
                        plist[index] = new_price
                        qlist[index] = new_quantity
                        totalprice += new_price
                        print(f"Quantity for {item_to_update} updated.")
                    else:
                        print("Item not found in the list.")
                elif choice == 3:
                    break
                else:
                    print("Invalid choice. Please try again.")

            discount = 0
            discount_choice = input("Do you have a discount coupon? (yes or no): ")
            if discount_choice.lower() == 'yes':
                discount = int(input("Enter discount percentage: "))
            
            if totalprice != 0:
                gst = (totalprice * 5) / 100
                discount_amount = (totalprice * discount) / 100
                finalamount = gst + totalprice - discount_amount
                
                print("\n" + "=" * 25 + " Kurnool Supermarket " + "=" * 25)
                print(" " * 28 + "Kurnool")
                print("Name:", name, " " * 30, "Date:", datetime.now())
                print("-" * 75)
                print(f"{'S.No':<5} {'Items':<15} {'Quantity':<10} {'Price':<10}")
                for i in range(len(pricelist)):
                    print(f"{i + 1:<5} {ilist[i]:<15} {qlist[i]:<10} {plist[i]:<10}")
                print("-" * 75)
                print(f"{'':<40} {'Total Amount:':<20} {'Rs':<5} {totalprice:<10}")
                print(f"{'GST Amount:':<40} {'':<20} {'Rs':<5} {gst:<10}")
                if discount > 0:
                    print(f"{'Discount Amount:':<40} {'':<20} {'Rs':<5} {-discount_amount:<10}")
                print("-" * 75)
                print(f"{'':<40} {'Final Amount:':<20} {'Rs':<5} {finalamount:<10}")
                print("-" * 75)
                print(" " * 50 + "Thanks for visiting")
                print("-" * 75)
                
                save_receipt = input("Would you like to save the receipt? (yes or no): ")
                if save_receipt.lower() == 'yes':
                    with open(f"receipt_{name}.txt", 'w') as f:
                        f.write("=" * 25 + " Kurnool Supermarket " + "=" * 25 + "\n")
                        f.write(" " * 28 + "Kurnool\n")
                        f.write(f"Name: {name} " + " " * 30 + f"Date: {datetime.now()}\n")
                        f.write("-" * 75 + "\n")
                        f.write(f"{'S.No':<5} {'Items':<15} {'Quantity':<10} {'Price':<10}\n")
                        for i in range(len(pricelist)):
                            f.write(f"{i + 1:<5} {ilist[i]:<15} {qlist[i]:<10} {plist[i]:<10}\n")
                        f.write("-" * 75 + "\n")
                        f.write(f"{'':<40} {'Total Amount:':<20} {'Rs':<5} {totalprice:<10}\n")
                        f.write(f"{'GST Amount:':<40} {'':<20} {'Rs':<5} {gst:<10}\n")
                        if discount > 0:
                            f.write(f"{'Discount Amount:':<40} {'':<20} {'Rs':<5} {-discount_amount:<10}\n")
                        f.write("-" * 75 + "\n")
                        f.write(f"{'':<40} {'Final Amount:':<20} {'Rs':<5} {finalamount:<10}\n")
                        f.write("-" * 75 + "\n")
                        f.write(" " * 50 + "Thanks for visiting\n")
                        f.write("-" * 75 + "\n")
                    print("Receipt saved successfully.")
                else:
                    print("Receipt not saved.")
            else:
                print("No items purchased.")
        elif main_choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
