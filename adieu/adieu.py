import inflect

p = inflect.engine()

names = []

done = False
while not done:
    try:
        name = input('Name: ')
        names.append(name)
    except EOFError:
        names_lst = p.join((names))
        print('\nAdieu, adieu, to ' + names_lst)
        done = True
