# buah = 'apple'

# h_huruf = []

# for huruf in buah:
#     h_huruf.append(huruf)

# print(h_huruf)


#comprehensions

# h_huruf = [huruf for huruf in buah]
# print(h_huruf)

#conditional comprehensions
# numbers = []

# for i in range(20):
#     if i % 2 == 0:
#         numbers.append(i)

# print(numbers)


numbers_list = [i for i in range(20) if i%2==0]
print(numbers_list)