customer_name = 'Alice'
cart_items = []
cart_prices = []

cart_items.append("Apple")
cart_items.append("Banana")
cart_items.append("Bread")
cart_prices.append(1.5)
cart_prices.append(0.75)
cart_prices.append(2.0)

cart_items.insert(1, "Milk")
cart_prices.insert(1, 2.5)

cart_items.remove('Banana')
cart_prices.remove(0.75)

cart_items.pop()
cart_prices.pop()

cart_items.sort()

total = 0
for item, price in zip(cart_items, cart_prices):
    print(f"{item}: ${price}")
    total += price

print(f'Cart total: {total}')
