starting_money = 100
starting_num_items = 10
item_price = 4

def buy_items(starting_money, starting_num_items, item_price):
    num_bought = 0
    while starting_money >= item_price and starting_num_items > 0:
            starting_money = starting_money - item_price
            starting_num_items = starting_num_items - 1
            num_bought += 1
    return num_bought

total = buy_items(starting_money, starting_num_items, item_price)
print("You were able to buy " + str(total) + " items.")

total_1 = buy_items(100, 10, 4)
print("Test 1: " + str(total_1))
total_2 = buy_items(10, 10, 4)
print("Test 2: " + str(total_2))