# Project 1:
customer_name = 'Alice'
cart_items = []
cart_prices = []

cart_items.append('Pizza')
cart_items.append('Banana')
cart_items.append('Bread')

cart_prices.append(1.5)
cart_prices.append(0.75)
cart_prices.append(2.0)

cart_items.insert(1, "Milk")
cart_prices.insert(1, 2.5)

cart_items.remove("Banana")
cart_prices.remove(0.75)

cart_items.pop()
cart_prices.pop()

cart_items.sort()

for price, item in zip(cart_prices, cart_items):
    print(f'{item}: ${price:.2f}')

total = sum(cart_prices)
print(f'Cart total: ${total:.2f}')


