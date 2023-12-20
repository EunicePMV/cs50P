# only accepts 25, 10 and 5
# check if correct
# then minus and print

coke = 50
change = 0
while coke != 0:
    print('Amount Due:' + amount_due)
    user_input = int(input('Insert a coin: '))
    if user_input == 25 or user_input == 10 or user_input == 5:
        amount_due = coke - user_input
    else:
        continue
    
