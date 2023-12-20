# only accepts 25, 10 and 5
# check if correct
# then minus and print

amount_due = 50
while amount_due > 0:
    print('Amount Due:' + amount_due)
    user_input = int(input('Insert a coin: '))
    if user_input == 25 or user_input == 10 or user_input == 5:
        amount_due = coke - user_input
    else:
        continue

print('Change Owed: ', abs(amount_due))
