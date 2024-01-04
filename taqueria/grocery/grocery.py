grocery_lst = {}

while True:
    try:
        item = input()
        if item in grocery_lst.keys():
            grocery_lst[item] =+ 1
        else:
            grocery_lst[item] = 1
    except EOFError:
        grocery_lst.sort()
        for key, value in grocery_lst.items():
            print(value, key.upper())

# count the number of items
# print in uppercase letter
# sort the items
