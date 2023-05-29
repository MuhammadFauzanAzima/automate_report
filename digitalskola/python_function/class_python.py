# class Customer:
#     """_summary_
#     function didalam class = method.
#     method parameternya harus diawali dengans self
#     self: method ini punyanya class Customer
#     """
#     def identity(self, new_name):
#         self.name = new_name
    
#     def identify(self):
#         print(f'customer name adalah {self.name}')


# customer1= Customer()
# customer1.identity("angga")
# # print(customer1.name)
# customer1.identify()


#Constructor __init__
# class Customer:
#     def __init__(self, name):
#         self.name = name

# customer1 = Customer("Angga")
# print(customer1.name)


#inheritance
#parent class
#super()
class Mobil():
    def __init__(self, color):
        self.color = color
    def desc(self):
        print("This is mobil", self.color)

#child class
class Honda(Mobil):
    def __init__(self, color, model):
        super().__init__(color)
        self.model = model

    def desc(self):
        print("this is honda", self.color, self.model)


ve = Mobil('Merah')
ho = Honda('Hitam', 'LCGC')

ve.desc()
ho.desc()