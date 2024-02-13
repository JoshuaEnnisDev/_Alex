def display_options():
    options = "(1) View Inventory (2) Add Item (3) Drop Item (4) Exit "
    choice = int(input(options))
    return choice


def view_inventory():
    print(f"{len(inventory)} items in your inventory")
    print(*inventory, sep=" -- ")


def add_item():
    add = input("What item do you want to add? ")
    inventory.append(add)
    print(f"{add} has been added to your inventory")
    

def drop_item():
    removed_item = input("What item do you want to remove? ")
    inventory.remove(removed_item)
    print(f"{removed_item} has been added to your inventory")


# list of items
inventory = ["shield", "sword", "arrows", "dagger"]


while True:
    selected_option = display_options()
    if selected_option == 1:
        view_inventory()
    elif selected_option == 2:
        add_item()
    elif selected_option == 3:
        drop_item()
    else:
        print("Goodbye!")
        break