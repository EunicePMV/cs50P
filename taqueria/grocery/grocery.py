grocery_lst = []

while True:
    try:
        item = input()
        grocery_lst.append(item)
    except EOFError:
        grocery_lst.sort()
        for item in grocery_lst:
            print(item.upper())

# count the number of items
