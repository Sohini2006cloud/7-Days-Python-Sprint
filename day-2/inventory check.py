products =["iphone","ipad","macbook","imac"]
price = [90000,45000,129000,290000]
product =input("Enter the name of the product you want:")
found= False
for index, item in enumerate(products):
    if item == product:
        print(f"{index}.{products} is in stock and the price is {price[index]}.")
        found= True
        break
    else:
        print("Sorry the item not found in inventory.")

