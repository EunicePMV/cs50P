menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
done = False
while not done:
    try:
        user_order = input('Item: ')
        price = menu[user_order.title()]
        total += price
        print('Total: $' + '{:.2f}'.format(total))
    except EOFError:
        done = True
        print('\n')
    except KeyError:
        continue
