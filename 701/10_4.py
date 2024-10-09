cart_items = ['Banana', 'Orange', 'Apple', 'Corn Bread']
cart_prices = [.3, .7, .2]

# for index in range(len(cart_items)):
#     print(f"{cart_items[index]}: ${cart_prices[index]}")
items = list(zip(cart_items, cart_prices))
items.sort()
cart_items.sort()

for item in items:
    print(f"{item[0]}: ${item[1]}")
print(sum(cart_prices))