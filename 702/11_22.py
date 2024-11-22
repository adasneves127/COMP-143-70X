def check_card(card_number):
    total = 0
    for i in range(len(card_number) - 1):
        if i % 2 != len(card_number) % 2:
            total += int(card_number[i])
        elif int(card_number[i]) > 4:
            total += 2 * int(card_number[i]) - 9
        else:
            total += 2 * int(card_number[i])
    return int(card_number[-1]) == (10 - (total % 10)) % 10


cards = open('card_nums', 'r')
for card in cards:
    print(f'{card.rstrip()} -- {check_card(card.rstrip())}')
cards.close()
