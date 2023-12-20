user_input = input('What is the Answer to the Great Question of Life, the Universe, and Everything?: ')
user_input = user_input.lower()
yes_ans = '42 forty-two forty two'

if user_input in yes_ans:
    print('Yes')
else:
    print('No')
