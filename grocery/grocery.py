grocery_lst = {}
done = False
while not done:
    try:
        item = input()
        if item in grocery_lst.keys():
            grocery_lst[item] += 1
        else:
            grocery_lst[item] = 1
    except EOFError:
        grocery_keys = list(grocery_lst.keys())
        grocery_keys.sort()
        grocery_lst = {i: grocery_lst[i] for i in grocery_keys}
        print()
        for key, value in grocery_lst.items():
            print(value, key.upper())
        done = True

# count the number of items
# print in uppercase letter
# sort the items
