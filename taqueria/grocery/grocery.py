grocery_lst = {}

while True:
    try:
        item = input()
        if item in grocery_lst.keys():
            grocery_lst[item] =+ 1
        else:
            grocery_lst[item] = 1
    except EOFError:
        print(grocery_lst)
        # grocery_keys = list(grocery_lst.keys()).sort()
        # grocery_lst = {i : grocery_lst for i in grocery_keys}
        # for key, value in grocery_lst.items():
        #     print(value, key.upper())

# count the number of items
# print in uppercase letter
# sort the items
