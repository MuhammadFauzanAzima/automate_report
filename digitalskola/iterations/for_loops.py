#List
# numbers = [6,5,3,23,2,3,5,23,5,6]

# sum = 0

# for num in numbers:
#     sum = sum + num
#     print(sum)

# print(f'Totalnya adalah {sum}')


#Dict {key:value}

dict_1 = {"name": "angga", "umur": 29, "pekerjaan": "expor-impor"}

# for key in dict_1.keys():
#     print(key)

# for value in dict_1.values():
#     print(value)

for key, value in dict_1.items():
    print(key, "->", value)