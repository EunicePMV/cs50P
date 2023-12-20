user_input = input('Give me a greeting: ')

if 'hello' in user_input:
    print('$0')
elif user_input[0] == 'h':
    print('$20')
else:
    print('$100')
