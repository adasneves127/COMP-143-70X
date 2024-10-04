cart_items = ['Banana','Orange','Apple', 'Corn Bread']
cart_prices = [0.3, 0.7, 0.1]

# total = 0
# for index in range(len(cart_items)):
#     print(f"{cart_items[index]}: ${cart_prices[index]}")
#     total = total + cart_prices[index]
# cart_total = sum(cart_prices)


print(list(zip(cart_items, cart_prices)))
items = list(zip(cart_items, cart_prices))
items.sort()

for item_pairs in items:
    print(f"{item_pairs[0]}: ${item_pairs[1]}")


