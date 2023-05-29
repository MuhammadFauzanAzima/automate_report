#user defined function
# mengambil 1 parameters
# def square(value):
#     """
#     Pangkat 2 operations
#     """
#     new_value = value ** 2
#     # print(new_value)
#     return new_value

# hasil = square(10)
# print(hasil)


#2 paramaters function
# def perkalian(angka1:int, angka2:int):
#     """_summary_:
#     Fungsi yang berguna untuk perkalian

#     Parameters
#     ----------
#     angka1 : Integer
#         _description_
#     angka2 : Integer
#         _description_

#     Returns
#     -------
#     Integer
#         _description_: Hasil perkalian
#     """
#     new_value = angka1 * angka2
#     return new_value

# hasil = perkalian(2,2)
# print(type(hasil))
# print(hasil)

# import os

# from python_function.square import return_multiple

# file_config = "/Documents/python_function/config.json"

#Return multiple values
def return_multiple(angka2, angka1=9):
    """
    Fungsi yang mengembalikan 2 values
    """
    perkalian = angka1 * angka2
    penambahan = angka1 + angka2

    # multiple_value = (perkalian, penambahan)

    return perkalian, penambahan

hasil = return_multiple(3)
print(hasil)
# # print(hasil[1])
# print(x)
# print(y)


# def loop1(value):
#     for i in value:
#         print(i)

# hasil = loop1(['a','b','c'])

# Paramater, *args, **kwargs
# def greet(*names):
#     for name in names:
#         print(f'Hello {name}')

# greet('Angga', 'Budi', 'Susi')


# def greet(**kwargs):
#     print('Hello', kwargs['first_name'], kwargs['last_name'])

# greet(first_name='Angga', last_name='Pradikta')



