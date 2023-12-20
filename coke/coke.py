# only accepts 25, 10 and 5
# check if correct
# then minus and print

user_input = int(input('Insert a coin: '))
coke = 50
change = 0
while coke != 0:
    amount_due = coke - user_input
    print('Amount Due:' + amount_due)
    user_input = int(input('Insert a coin: '))
