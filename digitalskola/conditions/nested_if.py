harga = 350
quantity = 350

if quantity > 200:
    # do something
    # pass
    if quantity > 500:
        print("Totalnya ada 500")
    elif quantity < 500 and harga > 300:
        print("Totalnya antara 300 dan 500")
    else:
        print("Totalnya antara 200 dan 500")
elif quantity == 200:
    print("Totalnya ada 200")
else:
    print("Totalnya kurang dari 200")