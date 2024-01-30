heading = '''
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        @                                         @
                        @                                         @
                        @           Josh's Jolly Treats           @
                        @                                         @
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
print(heading)

item_1 = "Vanilla Ice Cream"
item_2 = "Chocolate Ice Cream"

item_1_cost = 3.95
item_2_cost = 3.59

menu_items = f'''
                            {item_1}    {item_1_cost}
                            {item_2}    {item_2_cost}
'''
print(menu_items)
keep_shopping = True

answer = input("What would you like to buy? ").title()
while keep_shopping:
    if "Vanilla" in answer:
        quantity = int(input(f"How many {item_1}s would you like?"))
        total = item_1_cost * quantity

        print(f"Your total for {quantity} {item_2} is ${total}")
    elif answer == item_2:
        quantity = int(input(f"How many {item_2}s would you like?"))
        total = item_2_cost * quantity

        print(f"Your total for {quantity} {item_2} is ${total}")
    else:
        print(f"Sorry, we do not sell {answer}")



