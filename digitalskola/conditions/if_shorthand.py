# x=4
# if x==3:
#     print('x adalah 3')
# else:
#     print('different')

#Shorthand
# x=4
# if x==3: print('x adalah 3')
# print('x adalah 3') if x==3 else print('different')


#user input
name = input('Please input your name: ')
age = int(input('Input your age: '))

legal_status = 'dewasa' if age > 18 else 'anak kecil'

print(legal_status)